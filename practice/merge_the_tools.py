def merge_the_tools(string, k):
    sub = ""
    for index, char in enumerate(string):
        # print(index+1, k, (index+1)%k)
        if char not in sub:
            sub += char
        if (index+1) % k == 0:
            print(sub)
            sub = ""


if __name__ == "__main__":
    merge_the_tools("AABCAAADA", 3)
