#!/usr/bin/env python

import sys

def revstr(s):
    """ reverses the string and returns a list of characters """
    r = []
    
    for x in s:
	r.append(x)

    r.reverse()

    return r


def shiftcharright(clist, offset):
    """ shift character right by offset values """
    r = []
    for x in clist:
        c = ord(x)

        if c < 32: c = 32
        elif c > 125: c = 125
        
        if (c + offset) in (34, 39, 48, 49, 79, 108):
            c = c + (offset + 1)
        else: c = c + offset
        
        r.append(chr(c))
        
    return r


def main(a):
    print "Cur password:\t" + a[0]
    l = revstr(a[0])
    l = shiftcharright(l, 1)
    s = "".join(l)
    print "New password:\t" + s


if __name__ == '__main__':
    main(sys.argv[1:])
