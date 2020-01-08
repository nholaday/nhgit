#from the "sys" package, use the argv feaature = using the shell this imports an arguement
from sys import argv

#this sets the arguement to a variable called filename
script, filename = argv

#the arguement given was a filename and the vaiable txt is set to reference that file using open()
#also running open(filename) allows txt to be read.
txt = open(filename)

#prints filename's file name
print "Here is your file %r:" % filename
#prints txt which references filename
print txt.read()
filename.close()

#prompts for an input from the user for another file name and the name is stored as file_again
print "Type a filename to append:"
file_again = raw_input("> ")

#sets txt_again as a reference to file: file_again
txt_again = open(file_again)

#prints txt_again which refrences location of file: file_again
print txt_again.read()
file_again.close()
