def areSimilar(a, b):
    for i in range(len(a)-1):
        print(i)
        if a[i] != b[i]:
            if a[i] in b and not swapused:
                swapused = True
                a[i], b[b.index(a[i])] = b[b.index(a[i])], a[i]
            else:
                return False
    return True


a1 = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b1 = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]
if __name__ == "__main__":
    print(areSimilar(a1, b1))
