l1 = [1,2,4,8,16,32]
l2 = [1, 2, 3, 4, 5, 6]
l3 = [3,5,7,11,10]
l4 = range(2,100,3)
l5 = [1,1,1]

def answer(l):
    """Take highest element of list and check if mod == 0 for
    every other element in the list
    """
    triples = 0
    while len(l) > 0:
        factor_once = check_factor(l)
        #print("factor_once", factor_once)
        while len(factor_once) > 0:
            factor_twice = check_factor(factor_once)
            #print(factor_twice)
            if len(factor_twice) > 0:
                triples += len(factor_twice)
            #if check_factor_quick(factor_once):
            #    triples += 1
            #print("triples: {}".format(triples))
    #print("Answer------------------------------")
    return triples

def check_factor(l):
    """Pops the highest element on a list and checks if any of the other
    elements are divisors. Returns a list of all the divisors
    """
    divisors = []
    # print("check_factor on list:", l)
    current = l.pop()
    #print("current", current)

    for element in l:
        #print("current {} % element {} = {}".format(current, element, current % element))
        if current % element == 0:
            divisors.append(element)
        # don't keep checking factors above current / checkmax
        if element > current/2 > 1:  
            break

    return divisors

def check_factor_quick(l):
    """Same as check_factor but stops checking once it's found one match
    Returns 1 or 0 instead of a list
    """
    divisors = []
    # print("check_factor on list:", l)
    current = l.pop()
    #print("current", current)
    for element in l:
        #print("current {} % element {} = {}".format(current, element, current % element))
        if current % element == 0:
            return 1

    return 0


if __name__ == "__main__":
    print(answer(l1))
    print(answer(l2))
    print(answer(l3))
    print(answer(l4))
    print(answer(l5))
