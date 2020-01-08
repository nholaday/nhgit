# This program will get inputs from the user and compare them using definitions

def greater(a, b):
    print (a, b)
    if a > b:
        return True
    else:
        return False

val1 = int(raw_input("Value 1: "))
val2 = int(raw_input("Value 2: "))

print "Is Value 1 greater than Value 2: %r" % greater(val1, val2)
