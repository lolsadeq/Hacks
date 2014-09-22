#!/usr/bin/env python
# coding: utf-8

"""
Generates a crypted string from a password provided and a random salt.
For use when creating users with useradd or config managements tools such
as ansible
"""

from crypt import crypt
from string import ascii_letters, digits
from getpass import getpass
from random import choice


def main():
    match = False
    while not match:
        passwd = getpass()
        again = getpass(prompt="Password again: ")
        if passwd == again:
            match = True
        else:
            print 'No match! try again...'

    salt = ''.join(choice(ascii_letters + digits + './') for x in range(86))
    salt = '$6$%s$' % salt
    return crypt(passwd, salt)


if __name__ == '__main__':
    print main()
