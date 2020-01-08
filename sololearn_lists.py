from collections import deque
# Lists

list1 = [9,8,7,6,5,6]
print(list1)

# len is a function and is called before
print("len(list1) = %d" % len(list1))

# append and insert are methods of the list class and are called after with a dot
print("list1.append(11)")
list1.append(11)
print(list1)

# you can append multiple items with extend
print("list1.extend([20,21])")
list1.extend([20,21])
print(list1)

print("list1.insert(2,15)")
list1.insert(2,15)
print(list1)

# refer to single elements in a list by indices
print("list1[0], list1[-1]")
print(list1[0], list1[-1])

# index will search your list and return the index of the first entry if it is present. Otherwise will give a ValueError
print("list1.index(6) = %d" % list1.index(6))

# remove elements by index with del command
print("del list1[-2]")
del list1[-2]
print(list1)

# or by value by remove funcion
print("list1.remove(8)")
list1.remove(8)
print(list1)

print(max(list1))#: Returns the list item with the maximum value
print(min(list1))#: Returns the list item with minimum value
print(list1.count(6))#: Returns a count of how many times an item occurs in a list
list1.reverse()#: Reverses objects in a list
print(list1)

# pop deletes the last item of a list and returns it
popcorn = list1.pop()
print("popcorn = list1.pop()")
print("popcorn: {}, list1: {}").format(popcorn,list1)

nicelist1 = sorted(list1) # Returns the list sorted
print("nicelist1 = {}").format(nicelist1)

list1.sort() # Or sort() just sorts and replaces the list
print("after list1.sort() -> {}").format(list1)

# range() will create a list of sequential integers
print("range(10)", range(10))
print("range(3,10)", range(3,10))
print("range(3,10,3)", range(3,10,3))


# For queues it's more efficient to use deque than lists
# Queues are First in First out unlike lists(stacks) which are First in Last out
queue = deque([1,2,3,4,5])
queue.append(55)
print(queue)
print(queue.popleft())
print(queue)