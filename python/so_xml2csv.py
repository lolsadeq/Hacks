#!/usr/bin/env python3

"""
so_xml2csv.py - Converts stackoverflow xml dump data to csv format
Author: Jonas Gorauskas
Created: 2014-09-01 13:53:06
Modified: 2014-09-01 16:45:59
Description:

This script converts stackoverflow xml dump data to csv format for the purposes
of easy insertion into a SQL database such as Postgreql.

History:

    2014-09-01 13:53:06 - JGG
        Initial commit

"""

import xml.etree.ElementTreeas as etree
import argparse


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


def main():
    args = parse_args()


if __name__ == '__main__':
    main()
