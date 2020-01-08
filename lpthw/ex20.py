from sys import argv

script, input_file = argv

f = open(input_file)

# Prints the entire open file starting at wherever the marker is
def print_all(filein):
    print "First let's print the whole file: "
    print filein.read()

# Sets the marker for the file back to the beginning
def rewind(filein):
    print "Now let's rewind, kind of like a tape"
    filein.seek(0)

# defines a function that prints one line wherever the marker is for the file
def print_line(lineNumber, filein):
    print lineNumber,
    print filein.readline(),

print_all(f)

rewind(f)

counter = 1
print_line(counter, f)

counter += 1
print_line(counter, f)

rewind(f)

counter += 1
print_line(counter, f)

counter += 1
print_line(counter, f)

print_all(f)
