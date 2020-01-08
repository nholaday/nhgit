import random

def checkguess(gue,answer):
    ans = str(answer)
    bulls, cows = (0, 0)
    for i in range(4):
        print "g: %s, a: %s" %(gue[i], ans[i])
        if gue[i] == ans[i]:
            bulls += 1
            print "Bull", bulls
        elif gue[i] in ans:
            cows += 1
            print "Cow", cows
    return bulls, cows

def printbc(bulls,cows):
    if bulls == 1:
        print "1 bull, ",
    else:
        print "%d bulls, " % bulls,
    if cows == 1:
        print "1 cow"
    else:
        print "%d cows" % cows

if __name__ == "__main__":
    print "Cows and Bulls Game!"
    bulls = 0
    answer = random.randint(1000, 9999)
    print answer

    while not bulls == 4:
        guess = raw_input("Enter four digit number: ")

        bulls, cows = checkguess(guess, answer)
        printbc(bulls, cows)

        if bulls == 4:
            print "You Win, 4 Bulls!!"
