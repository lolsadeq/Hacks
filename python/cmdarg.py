#!/usr/bin/python

# some tests on command line parameters

import sys
import optparse

def main():
    p = optparse.OptionParser()
    p.add_option('--verbose', '-v', action='store_true')
    p.add_option('--name', '-n', default="world")
    options, arguments = p.parse_args()
    if options.verbose: print "Greetings and salutations,",
    else: print "Hello",
    print '%s!' % options.name

if __name__ == "__main__":
    main()




