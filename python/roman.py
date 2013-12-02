"""
Convert a Roman numeral to decimal and vice-versa
"""

import re

class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotIntegerError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass

roman_num_map = (('M', 1000),
                 ('CM', 900),
                 ('D', 500),
                 ('CD', 400),
                 ('C', 100),
                 ('XC', 90),
                 ('L', 50),
                 ('XL', 40),
                 ('X', 10),
                 ('IX', 9),
                 ('V', 5),
                 ('IV', 4),
                 ('I', 1))

roman_num_pattern = re.compile("""
    ^                 # start of string
    M{0,4}            # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})  # hundreds - 900, 400, 0-300 or 500-800
    (XC|XL|L?X{0,3})  # tens - 90, 40, 0-30, or 50-80
    (IX|IV|V?I{0,3})  # ones - 9, 4, 0-3 or 5-8
    $                 # end of string
    """, re.VERBOSE)

def to_roman(n):
    """ """
    if not (0 < n < 5000):
        raise OutOfRangeError, "number out of range (must be 1..4999)"
    if int(n) != n:
        raise NotIntegerError, "decimals can not be converted"

    result = ""
    for numeral, integer in roman_num_map:
        while n >= integer:
            result += numeral
            n -= integer

    return result


def from_roman(s):
    """ """
    if not s:
        raise InvalidRomanNumeralError, "input cannot be blank"
    if not roman_num_pattern.search(s):
        raise InvalidRomanNumeralError, "invalid roman numeral: %s" % s

    result = 0
    index = 0
    for numeral, integer in roman_num_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)

    return result
