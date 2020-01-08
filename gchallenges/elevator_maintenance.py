l1 = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
l2 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]

def answer(l):
    vlisted = []
    vstring = []
    
    for version in l:
        # Convert strings into lists of integers
        vlisted.append(list(map(int,version.split("."))))
    vlisted.sort()
    
    for v in vlisted:
        # Convert back to version number strings
        vstring.append(".".join(list(map(str, v))))
    return vstring

if __name__ == "__main__":
    print(answer(l1))
    print(answer(l2))
