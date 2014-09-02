#!/usr/bin/env python3

"""
so_xml2csv.py - Converts stackoverflow xml dump data to csv format
Author: Jonas Gorauskas
Created: 2014-09-01 13:53:06
Modified: 2014-09-01 17:04:21
Description:

This script converts stackoverflow xml dump data to csv format for the purposes
of easy insertion into a SQL database such as Postgreql.

History:

    2014-09-01 13:53:06 - JGG
        Initial commit

"""

import xml.etree.ElementTreeas as etree
import argparse
import time


class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-V', '--version',
                        action='version',
                        version='%(prog)s 0.1.0 - written by Jonas Gorauskas')
    parser.add_argument('-i', '--input', required=True, dest='input_file',
                        help='The input file to be processed')
    parser.add_argument('-o', '--output', required=True, dest='output_file',
                        help='The output file to save results to')
    parser.add_argument('-c', '--columns', required=True, dest='columns',
                        help='A comma delimited string denoting column order')

    return parser.parse_args()


def get_data(fn, columns):
    cols = columns.split(',')
    res = ''

    for col in cols:
        res = res + col + ','

    res = res[:-1] + '\n'

    tree = etree.parse(fn)
    root = tree.getroot()

    for row in root:
        if row.tag == 'row':
            for col in cols:
                if col in row.attrib:
                    if row.attrib[col].isnumeric():
                        res = res + row.attrib[col] + ','
                    else:
                        res = res + '"' + row.attrib[col] + '",'
                else:
                    res = res + ','
            res = res[:-1] + '\n'

    return res


def save_data(fn, data):
    with open(fn, 'w') as f:
        f.write(data)


def main():
    args = parse_args()
    with Timer() as t:
        data = get_data(args.input_file, args.columns)
        save_data(args.output_file, data)
    print('Done! Work took %.03f secs...' % t.interval)


if __name__ == '__main__':
    main()
