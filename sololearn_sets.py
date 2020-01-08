# sets are similar to lists but they cannot contain duplicate elements

set1 = {1,5,2,3,6,7,9,7,10}
print set1
print "len(set1): ", len(set1)
print "Does set1 have 3?", 3 in set1
for i in set1:
    print i,

set2 = set(["did","you","say","meow?"])
print "\n", set2
set2.add("never!")
set2.remove("did")
print set2

set3 = {9,5,4,1}
print "Union '|': ", (set1 | set3)
print "Intersetion: ", (set1 & set3)
print "Difference: ", (set1 - set3)
print "Symmetric difference: ", (set1 ^ set3)
