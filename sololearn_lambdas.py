import math

print math.pi

# Lambda functions are functions that are there to save space
# they can only have one line and can only be called once

#normal function
def subtract(x,y):
    return x - y
print subtract(5,3)
#lambda function
print (lambda x,y: x - y)(5,3)

#you can set a lambda to a variable to use multiple times
#but it's usually better to just define a function
lamadd = lambda x: x + x
print lamadd(3)
print lamadd(-6)
