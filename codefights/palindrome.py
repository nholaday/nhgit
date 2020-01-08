def checkPalindrome(inputString):
    for i in range(len(inputString)):
        print(inputString[i], inputString[(i+1)*-1])
        if inputString[i] != inputString[(i+1)*-1]:
            return False
    return True

checkPalindrome("asdfjkjsa")