l1 = [1,2,4,8,16,32]
l2 = [1, 2, 3, 4, 5, 6]
l3 = [3,5,7,11,10]
l4 = range(2,100,3)
l5 = [1,1,1]
l6 = [1,2,82,4,8,16,32]

def answer(l):
    """Iterate through the list. For each element check for how many factors
    come before that element on the list and how many multiples come after
    that element on the list.  
    Multiply those values together and add to a tally of Lucky Triples
    """
    triples = 0

    for i in range(1, len(l)+1):
        print(l[i-1])
        factors = check_factor(l[:i])
        multiples = check_multiple(l[i:], l[i-1])
        print factors, multiples, len(factors), len(multiples)
        #if len(factors) > 0 and len(multiples) > 0:
        triples += len(factors) * len(multiples)

    print("Answer------------------------------")
    return triples

def check_factor(flist):
    """Pops the highest element on a list and checks if any of the other
    elements are divisors. Returns a list of all the divisors
    """
    divisors = []
    # print("check_factor on list:", flist)
    current = flist.pop()

    for element in flist:
        #print("current {} % element {} = {}".format(current, element, current % element))
        if current % element == 0:
            divisors.append(element)

    return divisors

def check_multiple(mlist, current):
    """Checks if any of the elements in mlist are multiples of current.
    Returns a list of the multiples.
    """
    multiples = []
    # print("check_multiple on list:", mlist)

    for element in mlist:
        if element % current == 0:
            multiples.append(element)
    return multiples

if __name__ == "__main__":
    print(answer(l1))
    print(answer(l2))
    #print(answer(l3))
    #print(answer(l4))
    #print(answer(l5))
