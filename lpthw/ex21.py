def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

FirstVal = 8
SecondVal = 4
print "First Value: %d, Second Value: %d" % (FirstVal, SecondVal)
print "Added: %d\n" % add(FirstVal, SecondVal)
print "Subtracted: %d\n" % subtract(FirstVal, SecondVal)
print "Multiiplied: %d\n" % multiply(FirstVal, SecondVal)
print "Divided: %d\n" % divide(FirstVal, SecondVal)

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height %d, Weight %d, IQ: %d" % (age, height, weight, iq)

print "Here's a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
