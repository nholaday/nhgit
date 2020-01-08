# Createa program that asks the user for a number and then prints out a list of all the divisors of that number

def getinput():
    num = int(raw_input("Input a number: "))
    return num

def checkprime(num):
    for i in range(2,num/2+1):
        print "i,num: ", (i, num)
        if num % i == 0:
            return False
    return True

while True:
    number = getinput()
    if checkprime(number):
        print "Number is prime!"
    else:
        print "Number is not prime"
