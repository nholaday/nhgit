def adjacentElementsProduct(inputArray):
    largest = 0
    for i in range(len(inputArray) - 1):
        print inputArray[i], inputArray[i+1]
        if inputArray[i] * inputArray[i+1] > largest:
            largest = inputArray[i] * inputArray[i+1] 
    return largest

if __name__ == "__main__":
    print adjacentElementsProduct([3, 6, -2, -5, 7, 3])
