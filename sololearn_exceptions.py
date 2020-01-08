# If you receive an error you can specify what the program does using
# try and except ;D

from sys import argv

var = None

try:
    script, var = argv
    if var == "divzero":
        a = 1/0
except ZeroDivisionError:
    print "don't divide by zero!"
except ValueError:
    print "sololearn_exceptions.py <argument1>"
else:
    print "This will print if the 'try' succeeds"

if not var == None:
    print "Here is your arguement: %s" % var

# can be useful for user input
try:
    userinput = int(input("Enter Number >"))
    print "Here is your value * 5: %d" % (userinput * 5)
except:
    print "invalid input"
finally:
    print "This will print no matter what"

# assert can be used to ensure that variables are defined for troubleshooting
assert (not var == ""), "Needs an arguement!"

# you can manually raise errors with 'raise'
raise ImportError("Test!")
