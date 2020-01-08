def sortByHeight(a):
    b = []
    for item in a:
        if item > -1:
            b.append(item)

    b.sort()
    counter = 0
    for i in range(len(a)):
        if a[i] > -1:
            a[i] = b[counter]
            counter += 1

    return a


def betterSolution(a):
    b = sorted([i for i in a if i > -1])
    for n,item in enumerate(a):
        if item == -1:
            b.insert(n,item)
    return b

(sortByHeight(a = [-1, 150, 190, 170, -1, -1, 160, 180]))
