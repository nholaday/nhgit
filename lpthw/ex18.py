# defines a function that prints all arguements passed in
def print_all(*args):
    print "args: %r" % (args,)
    # another way to print all args:
    print "args:", args


# defines a function that only works with 2 arguements passed in
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2 %r" % (arg1, arg2)

# this just takes one arguement
def print_one(arg1):
    print "arg1:%r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."
    print_all("Zara", "Holaday")



print_all("Nic", "D", "Hola")
print_two_again("Nic2", "Hola2")
print_one("Nic")
print_none()
