# Make a two-player Rock-Paper-Scissors game
rps = {"rock":1, "scissors":2, "paper":3}
msg1 = "Player 1 Wins!"
msg2 = "Player 2 Wins!"

while True:
    player1 = raw_input("Player 1: ").lower()
    player2 = raw_input("Player 2: ").lower()

    diff = rps[player2] - rps[player1]

    if player1 == player2:
        print "Tie"
        continue
    elif player1 == "rock":
        if player2 == "scissors":
            print msg1
        else:
            print msg2
        break
    elif player1 == "scissors":
        if player2 == "paper":
            print msg1
        else:
            print msg2
        break
    elif player1 == "paper":
        if player2 == "rock":
            print msg1
        else:
            print msg2
        break
