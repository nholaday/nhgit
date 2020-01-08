# Createa program that asks the user for a number and then prints out a list of all the divisors of that number

num = int(raw_input("Enter a number: "))

divisors = []

for i in range(2,num/2+1):
    print "Checking :", i
    if num % i == 0:
        divisors.append(i)

print divisors
