from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "We will copy %r to %r" % (from_file, to_file)
print "Does the output file exist? %r" % exists(to_file)
print "This will delete what is in %r, to exit use CTRL-C to continue hit Enter" % to_file

raw_input("?")

#reading the from file
fromtarget = open(from_file)
contents = fromtarget.read()
print "The input file is %d bytes long" % len(contents)
fromtarget.close()

print "Here are the contents of %s: " % from_file
print contents

totarget = open(to_file, "w+")
totarget.truncate()
totarget.write(contents)
# contents2 = totarget.read()
# print "Here are the contents of %s: " % to_file
# print contents2
totarget.close()
