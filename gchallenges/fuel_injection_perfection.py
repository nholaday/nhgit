def answer(n):
    '''Always divide by 2 if it's even, if its odd, choose the neighbor 
    number that will divide to another even number as many times a possible
    This is the number that is divisible by the largest power of 2 
    '''
    n = int(n)
    opers = 0   # number of operations
    print("Running: ", n)

    while n > 1:
        print("n: {}, opers: {}".format(n, opers))
        if n % 2 == 0:  # if even divide by 2
            n /= 2
        elif n == 3:    # Special edge case, faster to subtract 1 than go to 4
            n -= 1
        else:
            if divis_power(n+1) > divis_power(n-1):
                n += 1
            else:
                n -= 1
        opers += 1
    return opers

def divis_power(x):
    '''Checks what the largest power of 2 the number is divisble by
    '''
    power = 1
    while x % 2**power == 0:
        power += 1
    # print("{} is divisible by 2^{}".format(x, power))

    return power



if __name__ == "__main__":
    for i in range(1, 16):
        print(answer(str(i)))
