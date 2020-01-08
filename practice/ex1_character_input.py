# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
#
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name = raw_input("Enter your name >")

while True:
    try:
        age = int(raw_input("Enter your age >"))
        msgcount = int(raw_input("How many messages >"))
        break
    except ValueError:
        print "Please enter an integer"

for i in range(msgcount):
    print "Hello %s, when you are 100 years old the year will be %d" % (name, 2017-age+100)
