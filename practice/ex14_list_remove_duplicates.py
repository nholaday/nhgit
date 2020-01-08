# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function

def remove_dup1(list1):
    return list(set(list1))

def remove_dup2(list1):
    newlist = []
    counter = 0
    for item in list1:
        addtolist = True
        for j in range(0,counter):
            print item, list1[j]
            if item == list1[j]:
                addtolist = False
                print "Not adding ", item
        if addtolist:
            newlist.append(item)
        counter += 1

    return newlist

def remove_dup3(list1):
    newlist = []
    for i in list1:
        if not i in newlist:
            newlist.append(i)
    return newlist

a = [6,1,3,5,5,6,8,8,9]
print remove_dup1(a)
print remove_dup2(a)
print remove_dup3(a)
