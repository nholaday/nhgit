def almostIncreasingSequence(sequence):
    print(sequence)
    for i in range(len(sequence)-1):
        print(i, sequence[i], sequence[i+1])
        if sequence[i] >= sequence[i+1]:
            if sequence[i+2] > sequence[i]:
                del sequence[i+1]
            else:
                del sequence[i]
            break
    if not removed:
        if sequence[len(sequence)-2] >= sequence[len(sequence)-1]:
            del sequence[len(sequence)-1]

    print(sequence)
    for i in range(len(sequence)-1):
        print(i, sequence[i], sequence[i+1])
        if sequence[i] >= sequence[i+1]:
            return False
    return True

print(almostIncreasingSequence([1, 2, 3, 4, 3, 6]))
