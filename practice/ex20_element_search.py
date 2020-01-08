# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
#
# Extras:
#
# Use binary search

a = [1,3,6,8,9,11,15]
element = 2

def is_inside(list1, element):
    if element in list1:
        return True
    else:
        return False

# def binarysearch(l, ele, beg, end):
#     if
#     elif l[(end-1) / 2] < ele:
#         binarysearch(l, ele, beg, end/2)
#     el

print is_inside(a, 2)
print is_inside(a, 3)
print is_inside(a, 4)

# for i in range(2,5):
#     print binarysearch(a, i, 1, len(a))
