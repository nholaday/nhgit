from sys import argv

script, filename3 = argv

text3 = open(filename3, "w")
print "\n%r is now open in mode: %r" % (text3.name, text3.mode)
print "Enter text to be saved in as %s" % filename3
enteredtext = raw_input("> ")
text3.write(enteredtext)
text3.close()

text3 = open(filename3, "r")
print "\n%r is now open in mode: %r" % (filename3, text3.mode)
print "Now here is that text read from your file: "
print text3.read()
