from copy import deepcopy

def matrixElementsSum(matrix):
    """First finds hmatrix which has all haunted rooms changed to zero,
    then iterates through whole matrix adding to sum and returns that value
    """
    for i in matrix:
        print(i)
    print("")
    markHauntedrooms(matrix)
    for i in matrix:
        print(i)

    sum = 0
    for i in matrix:
        for j in i:
            sum += j

    return sum

def markHauntedrooms(matrix):
    """Goes through matrix and wherever there is a 0
    changes below that position as 0
    Returns the modified (haunted) matrix
    """
    #hmatrix = deepcopy(matrix)
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if not matrix[y][x] and y != len(matrix)-1:
                matrix[y+1][x] = 0

    return matrix


if __name__ == "__main__":
    matrix1 = [[0, 1, 1, 2], 
               [0, 5, 0, 0], 
               [2, 0, 3, 3]]
    print(matrixElementsSum(matrix1))
