l1 = [i**1 % 25 for i in range(50)]
l2 = [i**2 % 25 for i in range(50)]
l3 = [i**3 % 25 for i in range(50)]

### Inserting this line will open a terminal to interact with the program
import pdb ; pdb.set_trace()

### Commands:
# l - lists where you are in program
# n - runs next line
# s - step in and dive deeper
# pp - pprint

l4 = []
for x, y in zip(l1, l2):
    l4.append(x + y)

