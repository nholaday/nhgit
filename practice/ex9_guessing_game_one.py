# Generate a random number between 1 and 9 (including 1 and 9).

import random

def initialize():
    count = 1
    ans = random.randint(1,9)
    return count, ans

def playGame():
    guesscount, answer = initialize()

    while True:
        userinput = raw_input("Enter your guess: ")
        if userinput == "exit":
            break

        guess = int(userinput)
        if guess == answer:
            print "Correct, you win!"
            print "You used %d guesses" % guesscount
            print ""
            guesscount, answer = initialize()
        elif guess < answer:
            print "Too low"
            guesscount += 1
        elif guess > answer:
            print "Too high"
            guesscount += 1

playGame()
