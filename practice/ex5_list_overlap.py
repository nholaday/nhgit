# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this
# Write this in one line of Python
 
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [random.randint(1,100) for i in range(10)]
d = [random.randint(1,100) for i in range(10)]


# can only do union with sets
print "a | b: ", list(set(a) | set(b))
print "c: ", c
print "d: ", d
print "c | d: ", list(set(c) | set(d))
