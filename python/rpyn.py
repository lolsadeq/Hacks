#!/usr/bin/env python

import math

stack = []

bbreak = False
bverb = False
bpnow = False

opstable = {
    '+': lambda x,y: y+x,
    '-': lambda x,y: y-x,
    '*': lambda x,y: y*x,
    '/': lambda x,y: y/x,
    '%': lambda x,y: y%x,
    '^': lambda x,y: y**x,
    '@': lambda x: abs(x)
    }

cmds = ['Q','P','C', 'H', 'V']

def execcmd(s):
    global stack
    global bbreak
    global bverb
    
    if s == 'H':
        printhelp()
    elif s == 'C':
        stack = []
        print stack
    elif s == 'P':
        print stack
    elif s == 'Q':
        print "bye..."
        bbreak = True   #To quit, signal the loop to exit
    elif s == 'V':
        bverb = not bverb
        if bverb:
            print "verbose mode on..."
        else:
            print "verbose mode off..."
    else:
        print "Command not recognized!"
        

def printhelp():
    print """
The following commands are available:

  H  Prints this help message
  Q  Quit RPYN
  C  Clears the stack
  P  Prints the stack
  V  Verbose output toggle

Use a single letter by itself at the prompt and
press <ENTER>. Case matters...
"""


def argcount(fn):
    c = fn.func_code
    return c.co_argcount

   
def main(): #Main program loop
    global bpnow
    
    print "RPYN - version 2.0"
    print "Reverse Polish Calculator written in Python"
    print "Use H for Help..."
    
    while True:
        s = raw_input("rpyn? ")
        
        if s in cmds:
            execcmd(s)
            if bbreak:
                break
            continue

        sa = s.split(' ')                                                       # parse input
        
        for si in sa:
            if si in opstable.keys():
                ac = argcount(opstable[si])
                if len(stack) < ac:
                    print "Not enough operands!"
                else:
                    bpnow = True
                    f = opstable[si]
                    if ac == 1:
                        stack.append(float(f(stack.pop())))                     # push [ pop ]
                    elif ac == 2:
                        stack.append(float(f(stack.pop(), stack.pop())))        # push [ pop, pop ]
                            

                if bverb and bpnow:
                    print " =    " + str(stack[-1])                             # peek - verbose
            else:
                bpnow = False
                try:
                    stack.append(float(si))                                     # push 
                except ValueError:
                    print "Not a valid operand!"
                    
        if not bverb and bpnow:
            print " =    " + str(stack[-1])                                     # peek - just ...

            
if __name__ == '__main__':
    main()
