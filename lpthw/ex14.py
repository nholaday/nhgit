from sys import argv

script, user_name, user2 = argv
prompt = 'gogogo>'

print "Hi %s and %s, I'm the %s script." % (user_name, user2, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input("type here")

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, you you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
