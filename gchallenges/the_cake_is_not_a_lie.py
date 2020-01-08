s1 = "abccbaabccba"
s2 = "xyzxyzxyzxyzaa"
s3 = "vvvvv"

def answer(s):
    seq = []
    for letter in s:
        if letter in seq:
            # This is a repeat letter, check if the first half
            # of the string so far is the same as the second half
            seq.append(letter)
            all_match = True
            for i in range(len(seq)/2):
                if (seq[i] != seq[i+len(seq)/2]):
                    all_match = False
            # if we found a pattern and it repeats for the rest
            # of the string, return the answer
            if all_match and check_sequence_continues(s, seq):
                return len(s) / (len(seq)/2)
        else:
            # print("Unique letter")
            seq.append(letter)
    # No repeating patterns found
    return 1

def check_sequence_continues(s, seq):
    counter = 0
    for letter in s:
        if letter != seq[counter]:
            return False
        else:
            counter += 1
        if counter >= len(seq)/2:
            counter = 0
    return True


if __name__ == "__main__":
    print(answer(s1))
    print(answer(s2))
    print(answer(s3))
