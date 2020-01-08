# ou, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
low = 0
high = 100

def step(lo, hi):
    return (hi - lo) / 2 + lo

while True:
    guess = step(low, high)
    print "Is this too low, too high or correct? ", guess
    reply = raw_input("> ").lower()
    if "high" in reply:
        high = guess
    elif "low" in reply:
        low = guess
    elif "correct" in reply:
        print "Yay"
        break
    else:
        print "Please type 'too high', 'too low', or 'correct.'"
