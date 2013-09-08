#!/usr/bin/env python

'''
File: dir-inventory.py
Author: Jonas Gorauskas [JGG]
Created: 2011-01-07 11:35:52
Modified: 2011-01-07 11:38:56
Description:

This script will recursively list the information about
files inside a root folder that is passed in as a parameter

History:

    2011-01-07 11:38:56 - JGG
        Initial version
'''

import os
import sys
import time
import stat
import argparse


def main():
    '''Main entry point for the script'''
    args = init()
    outlst = ['FilePath,FileSizeBytes,CreatedDate,ModifiedDate'] # Column headers
    flst = walk_tree(args.root_folder, visit_file, outlst)       # Get list of file information
    data = '\n'.join(['%s' % item for item in flst])             # Convert list to string data
    save_to_file(data, args.output_file)             
    

def init():
    '''Parse the command line parameters'''
    parser = argparse.ArgumentParser(description='Recursively lists the information about files inside a root folder that is passed in as a parameter')

    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s 0.1.0 - written by Jonas Gorauskas')
    parser.add_argument('-r', '--root', required=True,
                        help='The path to the folder to be inventoried',
                        metavar='FULL_PATH_TO_FOLDER', dest='root_folder')
    parser.add_argument('-o', '--output', required=True,
                        help='The path to the output file that will hold the data',
                        metavar='FULL_PATH_TO_OUTPUT_FILE', dest='output_file')
    
    return parser.parse_args()


def walk_tree(root_path, file_callback, out_list):
    '''Recursively walks down a directory tree and gather information about
    each file into a list'''
    for item in os.listdir(root_path):
        itempath = os.path.join(root_path, item)
        itemmode = os.stat(itempath)[stat.ST_MODE]
        
        if stat.S_ISDIR(itemmode):                  #this is a folder: recurse
            walk_tree(itempath, file_callback, out_list)
        elif stat.S_ISREG(itemmode):                #this is a regular file
            out_list.append(file_callback(itempath))
        else:                                       #this is something else: skip it
            pass
    
    return out_list


def visit_file(filepath):
    '''Gathers information about a single file in comma delimited format'''
    str_format = '"%s",%d,"%s","%s"'
    fileinfo = os.stat(filepath)
    created = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(fileinfo[stat.ST_CTIME]))
    modified = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(fileinfo[stat.ST_MTIME]))
    return str_format % (filepath, fileinfo[stat.ST_SIZE], created, modified)


def save_to_file(data, filepath):
    '''Saves the data to file path'''
    f = open(filepath, 'w')
    f.write(data)
    f.close()    


if __name__ == '__main__':
    main()
