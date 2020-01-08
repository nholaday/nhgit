# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print "a:", a

b = [i**2 for i in range(1,11)]
print "b:", b

c = [i**2 for i in range(1,11) if i % 2 == 0]
print "c:", c

d = [i for i in a if i % 2 == 0]
print "d:", d
