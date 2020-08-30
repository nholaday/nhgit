def minion_game(string):
    kevin = stuart = 0
    vowels = "AEIOU"
    for index in range(len(string)):
        if string[index] in vowels:
            kevin += len(string) - index
        else:
            stuart += len(string) - index

    if kevin > stuart:
        winner = "Kevin {}".format(kevin)
    elif stuart > kevin:
        winner = "Stuart {}".format(stuart)
    else:
        winner = "Draw"
    return winner

def old(string):
    for start in range(len(string)):
        subword1 = string[start:]
        for end in range(1,len(subword1)+1):
            subword2 = subword1[:end]
            if subword2[0] in vowels:
                kevin += 1
            else:
                stuart += 1

if __name__ == "__main__":
    print(minion_game("BANANA"))
