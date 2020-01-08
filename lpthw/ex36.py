import random

def start():
    print "You are a dog.  Do you want to play, eat, walk, or sleep?"
    a = raw_input("> ")
    if "play" in a:
        toy()
    elif "eat" in a:
        food()
    elif "walk" in a:
        walk()
    elif "sleep" in a:
        sleep()
    else:
        print "That is not somthing dogs do"
        start()

def toy():
    print "You see a bone and a rope, what do you take?"
    t = raw_input("> ")
    if "bone" in t:
        print "You start chewing on a bone but then--a paper towel?! nom nom nom."
    elif "rope" in t:
        rope()
    else:
        print "You pick the hidden option of daddy's sock"

# How do you get an input as an int without getting an error if they put in a string?
def food():
    print "How many times would you like to roll in your food before eating it?"
    roll = input("Type 0 or more> ")

    if roll >= 1:
        for i in range(0, roll):
             print "Mmmm smells so good let's roll in it!", i + 1
    else:
        print "That's not food it's just a rock!"

def walk():
    print "OMG another dog!"

def sleep():
    print "Sleep, HA!"
    start()

def rope():
    print "You grab the rope, do you run away or bring it to your person?"
    r = raw_input("> ")
    if "run" in r:
        circles = random.randrange(1, 50)
        print "You run in circles %s times, yet you still don't get dizzy!" % circles
        rope()
    elif "bring" in r or "person" in r:
        print "You bring it to your person, but for some reason they say \"ow!\", was it because you bit them?  They love you anyways :D"
    else:
        over("You stare blankly at your person for eternity")

def over(reason):
    print reason
    exit(0)



start()
