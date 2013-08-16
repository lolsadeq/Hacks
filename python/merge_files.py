#!/usr/bin/env python

'''
This will merge all the files in a directory into a single file. This is used
to aggregate several of the web server logs into a single source for processing
by awstats.
'''

import os
import sys
import time

from optparse import OptionParser


def list_files_in_dir(dir_path):
    """
    Generates a list of files in a directory

    Arguments:
    - `dir_path`: The path to the diretory to be listed
    """
    l = []
    for d, ds, fs in os.walk(dir_path):
        for f in fs:
            l.append(os.path.join(d,f))

    return l


def parse_options():
    check_options = True
    p = OptionParser()

    p.add_option('-?', dest='xhelp', action='store_true', help="display extended help message and exit")
    p.add_option('-V', dest='version', action='store_true', help="display version message and exit")
    p.add_option('-v', dest='verbose', action='store_true', help="display verbose output")
    p.add_option('-d', '--folder', dest='folder', help="The folder to scan")
    p.add_option('-o', '--out', dest='outfile', help="The output file")

    options, arguments = p.parse_args()

    if options.xhelp:
        usage()
        sys.exit(0)

    if options.version:
        version()
        sys.exit(0)

    if options.folder == None:
        print 'A valid folder path is a required parameter.'
        check_options = False

    if options.outfile == None:
        print "A valid output file name is a required parameter"
        check_options = False

    return (options, arguments, check_options)


def version():
    print 'merge_files.py - Merge Web Server Log Files into a Single File'
    print 'Version 0.2.0'
    print 'Written by Jonas Gorauskas'
    print


def usage():
    print
    print "Usage: mergeFiles.py -d|--folder <string> [-h|--help] [-?] [-V] [-v]"
    print
    print "    -?             Displays this extended help message and exits."
    print "    -V             Displays version number information and exits. "
    print "    -v             Displays verbose output. "
    print "    -d | --folder  The path to the folder to be scanned. This is "
    print "                   required."
    print "    -o | --out     The name of the merged file. It will be placed "
    print "                   in the same directory as option -d above."
    print
    print "Example:"
    print
    print "    mergeFiles.py -v -d C:\logfiles -o merged.log"
    print


def main(directory, outfile, v = false):
    """
    This is where all the merging gets done!
    Some notes about this function:

    1) Need to get the list of files prior to creating the output file or else
       the output file will also be in the list and that will cause an infinite
       loop

    2) I open the files as binary in Windows so that I can more easily avoid
       file corruption

    3) I read 100K bytes from a file at a time. Some of the files are fairly
       large (50MB) and if you read the entire file at once than you will use
       large chunck of memory. This keeps the memory footprint small and works
       faster

    Arguments:
    - `directory`: The directory where the files to be merged are
    - `outfile`:   The actual resulting merged file
    - `v`:         Verbose output on or off - off by default
    """

    t1 = time.time()
    fl = list_files_in_dir(directory)
    fout = file(os.path.join(directory, outfile), 'wb')

    for f in fl:
        if v: print 'Opening %s' % f

        fin = file(f, 'rb')

        if v: print '  Size: %d bytes' % os.path.getsize(f)

        while True:
            data = fin.read(102400)

            if not data:
                break

            fout.write(data)

        fin.close()

        if v: print 'Finished %s\n' % f

    fout.close()

    t2 = time.time()
    print 'Merged all %d files. Time taken: %0.3f ms\n\n' % (len(fl), (t2 - t1))


if __name__ == '__main__':
    opts, args, check = parse_options()
    if check:
        main(opts.folder, opts.outfile, opts.verbose)
    else:
        usage()
        sys.exit(0)


