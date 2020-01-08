l1 = range(1,101)

def binary_search(mylist, target):
    index = (len(mylist)-1)/2
    mini = 0
    maxi = len(mylist)-1

    while True:
        print mylist[index], index, mini, maxi
        if mylist[index] == target:
            return True
        elif target < mylist[index]:
            print "Less than"
            maxi = index - 1
            index -= (maxi - mini)/2
        else:
            print("Greater than")
            mini = index + 1
            index += (maxi - mini)/2
        raw_input()
    return False

if __name__ == "__main__":
    print(binary_search(range(1,101), 77))
