# Ask the user for a string and print out whether this string is a palindrome or not.

def is_palindrome(str):

    for i in range(len(str)):
        if not str[i] == str[len(str)-i-1]:
            return False
        print str[i],
        print str[len(str)-i-1]
    return True

word = raw_input("Enter a word: ")

if is_palindrome(word):
    print "Your word is a palindrome!"
else:
    print "Your word is not a palindrome"

# can also use:
print word, word[::-1]
if word == word[::-1]:
    print "this is a palindrome!"
