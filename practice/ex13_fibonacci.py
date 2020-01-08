# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate

def getfiblist(leng):
    fiblist = [1,1]
    for i in range(3,leng+1):
        print i
        fiblist.append(fiblist[i-3] + fiblist[i-2])
    return fiblist


length = int(raw_input("Length of Fibonacci Sequence: "))
print getfiblist(length)
