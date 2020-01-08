# This program will perform math operations on values passed to the function

def perform_math(val1, val2):
    print "First Value: %d, Second Value: %d" % (val1, val2)
    print "Added: %d" % (val1 + val2)
    print "Subtracted: %d" % (val1 - val2)
    print "Multiplied: %d" % (val1 * val2)
    print "Divided: %d" % (val1 / val2)
    print "Modulus: %d" % (val1 % val2)

print "\nHere is 1 and 2 passed directly to function: "
perform_math(1, 2)

print "\nHere is firstval ad secondval passed as integer variables: "
firstval = 10
secondval = 25
perform_math(firstval, secondval)

print "\nHere is math done in the arguements passed: "
perform_math(2+2, 4+6)

print "\nEnter two values to perform math on now: "
# firstval = int(raw_input("Input First Value: "))
# secondval = int(raw_input("Input Second Value: "))
# perform_math(firstval, secondval)
perform_math( int(raw_input("FirstVal: ")), int(raw_input("SecondVal: ")) )
