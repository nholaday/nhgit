# dir() shows local variables or attributes
x = [1,2,3,4]
print(dir())
print(dir(x))

# vars() also prints values
print(vars())
from itertools import chain
print(vars(chain))
