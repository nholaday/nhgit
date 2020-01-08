from sys import argv

script, filename = argv

print "Your file name is: %r" % filename

#opens file for appending
ref = open(filename, "a")
app = ref.name()
print "Here is your appended file:"
