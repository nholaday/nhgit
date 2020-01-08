ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list.  Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) < 10:
    nextthing = more_stuff.pop()
#    print "Adding: ", nextthing,
    stuff.append(nextthing)
#    print "There are now %d items in stuff" % len(stuff),

count = 1
for i in stuff:
    print i,
    print count
    count += 1

print "Let's do some things with stuff."

print "Item 1(second item) is: %r" % stuff[1]
print "Last item is: %r" % stuff[-1]
print "Using stuff.pop(): %r" % stuff.pop()
print "Using \' \'.join(stuff): %r" % ' '.join(stuff) # What? cool!
print "Using '#'.join(stuff[3:5]): %r" % '#'.join(stuff[3:5]) # super stellar!
