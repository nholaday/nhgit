from itertools import combinations

def answer(banana_list):
    """Use itertools.combinations to find every combo of 2 guards.
    Play the game with each combo, if they are equal fail, if they get to any
    of the tuples they've already had (inverted too) it passes.
    
    Then need to figure out if mutliple passes on a single guard which to
    pair him up with.
    """
    banana_list.sort()
    bdict = {}
    matches = []
    for ban in banana_list:
        bdict[ban] = []
    combos = combinations(banana_list, 2)
    for combo in combos:
        if play_game(combo):
            matches.append(combo)
            bdict[combo[0]].append(combo[1])
    #print matches
    print(bdict)
    #if matches != []:
    #    find_matches(matches, [], 0)

def find_matches(matches, uniqlist, index):
    """This function finds the maximum amount of matches possible with the
    matches found from play_game
    """
    print matches[index], index, uniqlist
    if (matches[index][0] in uniqlist) or (matches[index][1] in uniqlist):
        print index
    else:
        uniqlist.append(matches[index][0])
        uniqlist.append(matches[index][1])
    index += 1
    find_matches(matches, uniqlist, index)

def play_game(combo):
    """Takes a tuple of 2 ints and returns True if the game goes on forever
    """
    a, b = combo
    past_games = []
    #print a, b
    
    while True:
        if b < a:   # swap to always have (a) lower
            a, b = b, a
        past_games.append((a, b))
        #print(a, b)
        #print(past_games)
        if a == b:
            return False
        elif a < b:
            b -= a
            a *= 2
        else:
            print("This should not happen")
        if (a, b) in past_games:
            return True
    

if __name__ == "__main__":
    l1 = [1, 7, 3, 21, 13, 19, 54,55,56,58,59,67]
    l2 = [1, 7, 3, 21, 13, 19]
    
    #print(answer(l1))
    print(answer(l2))
