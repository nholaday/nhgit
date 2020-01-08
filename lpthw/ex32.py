the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']

change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

#same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

#also we can go through mixed lists
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
# range returns a list of integers starting with the first value and ending with the last
# range (first int, last int minus one, step)

for i in range (1, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)
    print "Now here is the full list: %r" % elements
#elements = range(1, 6)

# now we can print them out too
for i in elements:
    print "Element was : %d" % i
