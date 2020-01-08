def allLongestStrings(inputArray):
    maxlen = 0
    for item in inputArray:
        if len(item) > maxlen:
            outputArray = [item]
            maxlen = len(item)
        elif len(item) == maxlen:
            outputArray.append(item)
    return outputArray

print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))
