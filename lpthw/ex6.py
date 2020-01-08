x = "There are %d types of people." % 10 #puts integer 10 where %d is
#defining strings
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not) # puts the 2 strings inside another string called y

print x
print y

print "I said: %r." % x # prints x with '' around it
print "I also said: '%s'." % y # prints only string y with no quotes

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r" # defines a string that needs a % string after it in order to complete the statement

print joke_evaluation % hilarious # prints joke_evaluation inputting hilarious in the %r spod defined from before

w = "This is the left side of..."
e = "a string with a right side."

print w + e # slaps 2 strings together
