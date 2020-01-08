l1 = [4, 2, 9, 1, 10, 2, 8, 1]
l2 = [1, 2, 3, 4]

def answer(l, t):
    """Whatever index your at, count backwards and add the previous 
    entries to see if you can add up to the target.  If you find the 
    target you're done.  If you exceeded the target break.
    """
    counter = 0
    for entry in l:
        # Check if this index matches target
        backcount = counter
        sum = 0
        while (backcount > -1):
            sum += l[backcount]
            if sum == t:
                # Found match! 
                return (backcount, counter)
            elif sum >= t:
                break
            backcount -= 1
        counter += 1
    return(-1, -1)

if __name__ == "__main__":
    print(answer(l1, 12))
    print(answer(l2, 15))
    print(answer(l1, 9))

