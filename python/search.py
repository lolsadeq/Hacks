#!/usr/bin/env python

import os
import sys
from optparse import OptionParser

def main(basedir, searchterm):
    f = open('scanoutput.txt', 'w')
    f.write('\n'.join(get_files(basedir, searchterm)))
    f.close()
    print 'DONE'

def get_files(bdir, term):
    l = []
    for d, ds, fs in os.walk(bdir):
        for f in fs:
            s = d + '/' + f
            if term in s:
                l.append(s)
    return l

def parse_options():
    check_options = True
    p = OptionParser()

    p.add_option('-d', '--basedir', dest='dir', help="The directory to scan")
    p.add_option('-s', '--search', dest='search', help="String to search for")

    options, arguments = p.parse_args()

    if options.dir == None:
        print 'A valid directory is required'
        check_options = None

    if options.search == None:
        print 'A valid search term is required'
        check_options = None

    return (options, arguments, check_options)

if __name__ == '__main__':
    opts, args, check = parse_options()
    if check:
        main(opts.dir, opts.search)
    else:
        print 'ERROR'
        sys.exit(0)


# [~/] what now... $ python search.py -d ~/Desktop/ToArchive/ -s .mp3
# [~/] what now... $ python search.py -d ~/Desktop/ToArchive/ -s .mp3
# [~/] what now... $ python search.py -d ~/Desktop/ToArchive/ -s .ogg
