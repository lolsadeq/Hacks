#!/usr/bin/env python

"""A study in randomness:

Given the function get_id(size) below, that generates an ID of a certain lenght
from a set of uppercase letters A-Z and digits 0-9, how long in characters does
the ID need to be to avoid collisions in the generated samples at 1, 2.5, 5, and
10 million samples?

Ran on 2013-12-08 17:09:05:

Sample Size: 1000000; ID Size: 6; Collisions: 457; LCR: 2;
Sample Size: 1000000; ID Size: 7; Collisions: 21; LCR: 2;
Sample Size: 1000000; ID Size: 8; Collisions: 0; LCR: 0;
Sample Size: 1000000; ID Size: 9; Collisions: 0; LCR: 0;
Sample Size: 1000000; ID Size: 10; Collisions: 0; LCR: 0;
Sample Size: 2500000; ID Size: 6; Collisions: 2704; LCR: 3;
Sample Size: 2500000; ID Size: 7; Collisions: 98; LCR: 2;
Sample Size: 2500000; ID Size: 8; Collisions: 10; LCR: 2;
Sample Size: 2500000; ID Size: 9; Collisions: 0; LCR: 0;
Sample Size: 2500000; ID Size: 10; Collisions: 0; LCR: 0;
Sample Size: 5000000; ID Size: 6; Collisions: 10672; LCR: 3;
Sample Size: 5000000; ID Size: 7; Collisions: 378; LCR: 2;
Sample Size: 5000000; ID Size: 8; Collisions: 12; LCR: 2;
Sample Size: 5000000; ID Size: 9; Collisions: 0; LCR: 0;
Sample Size: 5000000; ID Size: 10; Collisions: 0; LCR: 0;
Sample Size: 10000000; ID Size: 6; Collisions: 42472; LCR: 3;
Sample Size: 10000000; ID Size: 7; Collisions: 1495; LCR: 2;
Sample Size: 10000000; ID Size: 8; Collisions: 51; LCR: 2;
Sample Size: 10000000; ID Size: 9; Collisions: 0; LCR: 0;
Sample Size: 10000000; ID Size: 10; Collisions: 0; LCR: 0;
"""

import random
import collections

# All uppercase chars A-Z and digits 0-9
samp_lst = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71,
            72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
            90]

# Sample counts
samp_cnt = [1000000, 2500000, 5000000, 10000000]

# ID sizes
id_sizes = [6, 7, 8, 9, 10]

def get_id(size_of_id):
    smp = random.sample(samp_lst, size_of_id)
    random.shuffle(smp)
    return ''.join(['%s' % chr(c) for c in smp])


def get_sample(id_size, samp_count):
    return [get_id(id_size) for i in range(samp_count)]


def find_collisions(sample):
    return [(y, x) for x, y in collections.Counter(sample).items() if y > 1]


if __name__ == '__main__':
    for count in samp_cnt:
        for size in id_sizes:
            smp = get_sample(size, count)
            cll = find_collisions(smp)
            cll.sort()
            print 'Sample Size: %d; ID Size: %d; Collisions: %d; LCR: %d;' \
                  % (len(smp), size, len(cll), 0 if len(cll) == 0 else cll[-1][0])
