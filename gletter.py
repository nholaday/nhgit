import string

print "Guess the number!"

def get_random_word():
    return "testing"

def play_game():
    word = get_random_word()
    wordlist = string.split(word, "")

    #while (strikes < 3):
    #    word.split
    print word
    print wordlist

play_game()
