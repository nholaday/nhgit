# Loops

listx = ["here","is","a","group","of","words"]

# prints all things in list
for word in listx:
    print word,

print ""
# goes through loop certain amount of times
for num in range(4,10):
    print num,

counter = 1
while True:
    print "while loop"

    if counter <=3:
        counter += 1
        print "'continue' starts loop over, counter = %d" % counter
        continue

    print "break kills the loop"
    break

# enumerate() will also give a counter in for loops
# can use instead of for i in range(len(listx))
for index, word in enumerate(listx):
    print("'{}' is the {}th word".format(word, index))

# zip() can be used when iterating over 2 lists at once
listy = [5,9,18,4,5,6,7,10]
for word, num in zip(listx, listy):
    print("{} -- {}".format(word, num))

# reversed() returns an iterator for the reversed list
print(reversed(listx))
for word in reversed(listx):
    print(word),

# all() and any()
print([word == "group" for word in listx])
print("any: {}".format(any([word == "group" for word in listx])))
print("all: {}".format(all([word == "group" for word in listx])))