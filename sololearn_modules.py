# import modules and use .var to call functions and variables
# you can import specific methods or variables with from __ import __

# how can you tell what is in the module?
# is there a module reference?


import random
from math import pi, sqrt, cos as cosine

for i in range(1,11):
    print(random.randint(1,20))

print pi
print sqrt(36)
print cosine(pi)

def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)
