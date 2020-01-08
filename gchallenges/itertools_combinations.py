from itertools import combinations

def answer(l):
    combos = combinations(l,3)
    triples = 0
    for c in combos:
        if c[0] < c[1] < c[2]:
            if c[2] % c[1] == c[1] % c[0] == 0:
                #print(c)
                triples += 1
    return triples

l1 = [1,2,7,3,4,5,6]
if __name__ == "__main__":
    print(answer(l1))

