#!/usr/bin/env python

'''
File: pwgen.py
Author: Jonas Gorauskas [JGG]
Description: Generates Rnadom Passwords
Created: 2007-11-13 12:05:15 

History:

    2007-11-13 12:05:15 - JGG
        Initial version

    2010-04-14 15:11:30 - JGG
        Removed sum function
'''

import sys
import random
import optparse

symbols = [33, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126]
lcalpha = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
ucalpha = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
digits = [50, 51, 52, 53, 54, 55, 56, 57]

_cnt = 0
_dgt = 0
_len = 0
_loc = 0
_sbl = 0
_upc = 0

def main():
    """Main entry point and where are the work is done"""
    init()
    for i in range(_cnt):
        l = random.sample(symbols, _sbl)
        l += random.sample(lcalpha, _loc)
        l += random.sample(ucalpha, _upc) 
        l += random.sample(digits, _dgt)
        random.shuffle(l)
        s = ''.join(['%s' % chr(x) for x in l])
        print s


def init():
    """Parse the command line and initialize the whole thing"""
    global _cnt
    global _dgt
    global _len
    global _loc
    global _sbl
    global _upc

    p = optparse.OptionParser()

    p.add_option('-?', dest="xhelp", action='store_true', help="display extended help message and exit")
    p.add_option('-V', dest="version", action='store_true', help="display version message and exit")
    p.add_option('-c', dest="count", default=1, help="how many passwords to generate")
    p.add_option('-d', dest="digit", default=1, help="how many digits to include")
    p.add_option('-L', dest="length", default=8, help="length of password in characters")
    p.add_option('-l', dest="lcase", default=0, help="how many lower case characters to include")
    p.add_option('-s', dest="symbol", default=1, help="how many symbols to include")
    p.add_option('-u', dest="ucase", default=1, help="how many upper case characters to include")

    options, arguments = p.parse_args()

    if options.xhelp:
        usage()
        sys.exit(0)

    if options.version:
        version()
        sys.exit(0)

    _cnt = int(options.count)
    _dgt = int(options.digit)
    _len = int(options.length)
    _loc = int(options.lcase)
    _sbl = int(options.symbol)
    _upc = int(options.ucase)

    # apply some business rules here
    if sum(list((_dgt, _sbl, _upc))) >= _len:
        _loc = 0
    elif sum(list((_dgt, _loc, _sbl, _upc))) > _len:
        _len = sum(list((_dgt, _loc, _sbl, _upc)))
    elif sum(list((_dgt, _sbl, _upc))) < _len:
        _loc = _len - (sum(list((_dgt, _sbl, _upc))))


def version():
    print 'pwgen.py - Generates Random Passwords'
    print 'Version 0.2.0'
    print 'Written by Jonas Gorauskas'
    print 


def usage():
    print "Usage: pwgen.py [-h|--help] [-?] [-V] [-c <int>] [-d <int>] [-L <int>]"
    print "                [-l <int>] [-s <int>] [-u <int>] "
    print 
    print "    -?      Displays this extended help message and exits."
    print "    -V      Displays version number information and exits. "   
    print "    -c      How many passwords to generate. Default is 1."
    print "    -d      Digit characters to include in passwords. Default is 1."
    print "    -L      Password length in characters. Default is 8."
    print "    -l      Lower case characters to include in password. If this value"
    print "            is provided than the sum of characters overrides the --len"
    print "            parameter. Default is the sum of symbol, digit, uppercase"
    print "            characters minus the length of the password."
    print "            e.g.: if symbol = 2 and digit = 2 and uppercase = 3 and"
    print "                  lenght = 12 then lowercase = 5"
    print "    -s      The number of symbols to include in the passwords. Default"
    print "            is 1."
    print "    -u      Upper case characters to include in password. Default is 1."
    print 
    print "Examples:"
    print 
    print "    pwgen.py"
    print 
    print "        Prints one password with a length of 8 characters, containing"
    print "        one symbol, one digit and one uppercase letter."
    print 
    print "    pwgen.py -c10 -L10 -d2 -s2 -u2"
    print 
    print "        Prints 10 passwords, one per line, with a length of 10"
    print "        characters each, each containing 2 digits, 2 symbols, and 2"
    print "        uppercase characters"
    print 
    print "Notes:"
    print 
    print "    This generator omits the following characters: \", \', 0, 1, O, l."
    print "    That is the double quote, single quote, the numbers zero and one,"
    print "    and the letters capital O and lowercase L, respectively."
    print
    print "    A minimally secure password is one which has at least 8 characters"
    print "    in length and contains at least one digit character, one symbol"
    print "    character and one upper case character."
    print 


if __name__ == '__main__':
    main()  

