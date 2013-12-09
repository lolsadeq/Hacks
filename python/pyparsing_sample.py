#!/usr/bin/env python

from random import choice
from pyparsing import *

tests = ['Hello, World!', 'Hi, Mom!', 'Good morning, Miss Crabtree!', 'Yo, Adrian!', 'Whattup, G?', "How's it goin', Dude?", 'Hey, Jude!', 'Goodbye, Mr. Chips!']

word = Word(alphas + "'.")
salutation = OneOrMore(word)
comma = Literal(',')
greetee = OneOrMore(word)
endpunc = oneOf('! ?')
greeting = salutation + comma + greetee + endpunc

print tests
print

for t in tests:
    results = greeting.parseString(t)
    print results

print

for t in tests:
    results = greeting.parseString(t)
    salutation = []
    for token in results:
        if token == ',': break
        salutation.append(token)
    print salutation

print

word = Word(alphas + "'.")
salutation = Group(OneOrMore(word))
comma = Suppress(Literal(","))
greetee = Group(OneOrMore(word))
endpunc = oneOf('! ?')
greeting = salutation + comma + greetee + endpunc


for t in tests:
    res = greeting.parseString(t)
    print res

print

for t in tests:
    results = greeting.parseString(t)
    salutation = []
    for token in results:
        if token == ',': break
        salutation.append(token)
    print salutation

print

for t in tests:
    salut, greet, endp = greeting.parseString(t)
    print salut, greet, endp

print

salutes = []
greets = []

for t in tests:
    salut, greet, endp = greeting.parseString(t)
    salutes.append((' '.join(salut), endp))
    greets.append(' '.join(greet))

for i in range(50):
    print '%s, %s%s' % (choice(salutes)[0], choice(greets), choice(salutes)[1])

print

for i in range(20):
    print '%s, say "%s" to %s.' % (choice(greets), ''.join(choice(salutes)), choice(greets))

print
