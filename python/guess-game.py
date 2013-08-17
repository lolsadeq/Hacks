#!/usr/bin/env python

"""a guessing game...
guess a number between 1 and 10 and see if you guessed right"""

import random

def main():
    name = str(raw_input("What's your name? "))
    print "Hello, %s" % name
    print "This is a guessing game..."

    while(True):
        choice = random.choice(range(1,11))
        guess = int(raw_input("Please guess a number between 1 and 10: "))

        if choice == guess:
            print "YOU WIN!!! Your guess was %d and the computer's choice was %d also..." % (guess, choice)
        else:
            print "You Lose! Your quess was %d and the computer's choice was %d..." % (guess, choice)

        if str(raw_input("Would you like to try again (yes/no)? ")) == "no":
            break

    print "This game was fun and we should try again soon... Bye!"


if __name__ == '__main__':
    main()
