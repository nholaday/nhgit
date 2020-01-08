# Created by Nic Holaday 2017
import random

print "Welcome to the dice roller"

diceart = [
""" -----
|     |
|  o  |
|     |
 -----""",
""" -----
| o   |
|     |
|   o |
 -----""",
""" -----
| o   |
|  o  |
|   o |
 -----""",
""" -----
| o o |
|     |
| o o |
 -----""",
""" -----
| o o |
|  o  |
| o o |
 -----""",
""" -----
| o o |
| o o |
| o o |
 -----"""]

while True:
	for die in range(2):
		print diceart[random.randint(0,5)]
	userinput = raw_input("Press Enter to roll again...")
	if not userinput == "":
		break
