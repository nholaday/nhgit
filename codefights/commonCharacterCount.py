def mySolution(s1, s2):
    total = 0
    list2 = list(s2)
    for char in s1:
        if char in list2:
            total += 1
            list2.remove(char)
    return total

# Better Solution
def commonCharacterCount(s1, s2):
    """Use list comprehension to make one line for loop.
    count will count how many times the character is in that string.
    set() finds the unique characters in a string
    """
    # creates a list of number of times each character shows up
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(com)

# from collections import Counter
# Counter works a lot like bash command "uniq -c"
# it counts how many times a character shows up and makes a dict