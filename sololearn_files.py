# read mode
# text = open("text1.txt", "r")
text = open("text1.txt")

content = text.read()
print content
text.close()

text = open("text1.txt")
# readlines returns a list of lines
lines = text.readlines()
print lines
text.close()

# write mode, thw write method returns the length of the string
text = open("text1.txt", "w")
length = text.write("Deleting whatever is in text1.txt and Writing this line to file")
print length
text.close()

# to ensure files always close you can use try and finally
# this will close the file even if there is an error
try:
    text = open("text1.txt")
    print "Print using try, finally"
    print text.read()
finally:
    text.close

# you can also do this automatically using 'with'
with open("text1.txt") as f:
    print "Print using with"
    print f.read()
# this automatically closes the file as well
