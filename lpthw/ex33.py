numbers = []

# def numappend(lista):
#     i = 0
#     runloop = i < 7
#     while runloop:
#         lista.append(i)
#         print "Lista: ", lista
#         i += 1
#         runloop = i < 7
#     return lista

## same thing with a for loop
def numappend(lista):
    for i in range(0, 7):
        lista.append(i)
        print "Lista: ", lista

    return lista


print "numbers before: ", numbers
numappend(numbers)
print "numbers after: ", numbers

# without using the function
# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#
#     i += 1
#     print "numbers now: ", numbers
#     print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num,
