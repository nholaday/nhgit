# Dictionaries, Tuples and Lists
dic = {
    3:"zoo",
    7:"stapler",
    9:"red"
}
print dic
print dic[7]
dic[14] = "alakazam"
print dic
# is key '9' in dictionary dic
print 9 in dic
# the get method returns a none or specified value if the key is not found
# instead of giving an error
print dic.get(14)
print dic.get(8)
print dic.get(8,"8 is Not found!")
# to get just the values use .values() and keys .keys()
print "just values: {}".format(dic.values())
print "just keys: {}".format(dic.keys())
# use update() to add multiple pairs
dic.update({12:"stuff", 24:"koala"})
# Removing a key
dic.pop(7)

# Tuples - immutable, lists that cannot be changed
wordtuple = ("liter","of","cola")
print wordtuple[0]

# Lists can be changed
wordlist = ["don't","want","a","large","farva"]
print wordlist
wordlist[0]="ooo"
print wordlist
# list Slice
print "list slice: ", wordlist[2:4]
print "list slice end: ", wordlist[2:]
# list slice with step
print "list slice every other: ", wordlist[::2]
# negative numbers count from the end
print "list skipping first and last: ", wordlist[1:-1]
# this reverses lists
print "Reversed list: ", wordlist[::-1]

# List comprehensions
squares = [i**2 for i in range(1,11)]
print "Squares: ", squares
squares2 = [i**2 for i in range(1,11) if not i**2 == 36]
print "Squares2: ", squares2

# If statements can also be written on one line with this format
print("Yes" if True else "No")

# defaultdict is a dictionary that uses a default key to create a new entry if a key is attempted to be accessed that does not exist
import collections
defaultani = collections.defaultdict(str)
print defaultani["cat"]  #creates entry {'cat': ''}
print defaultani

ani = {}
try:
    print ani["cat"]
except KeyError:
    print 'ani["cat"] causes Key Error'

deflist = collections.defaultdict(list)
deflist['pog'].append(1)
print deflist
