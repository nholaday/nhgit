# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#
#   My name is Michele
# Then I would see the string:
#
#   Michele is name My
# shown back to me

phrase = raw_input("Enter phrase: ")

def reverse_phrase(phrase):
    forw = phrase.split(' ')
    print forw

    rev = forw[::-1]
    print rev

    revphrase = (' ').join(rev)

    return revphrase

print reverse_phrase(phrase)
