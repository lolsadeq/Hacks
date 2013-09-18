
print
print "Multiplication Table"
print

nums = (1,2,3,4,5,6,7,8,9,10)

for n in nums:
    print "\t%i" % n,

print
print "=" * 90

for n1 in nums:
    print "%i" % n1,

    for n2 in nums:
        print "\t%i" % (n1 * n2),

    print
    print "-" * 90
