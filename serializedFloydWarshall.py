import numpy as np
import time

def readMatrix(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    matrix = []

    for row in lines:
        matrix.append([int(j) for j in row.split()])

    file.close()
    return np.array(matrix)

def writeMatrix(filename, matrix):
    file = open(filename, 'w')
    for row in matrix:
        file.write(str(row)[1 : -2] + '\n')
    file.close()

def floydWarshallSerialized(matrix):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    return np.array(matrix)


if __name__ == '__main__':

    choice = int(input('1. Read From File\n2. Enter Manually\n3. Default Matrix\n\n:'))

    if choice == 1:
        filename = input('\nEnter File Name: ')
        inputMatrix = readMatrix(filename)
    
    elif choice == 2:
        n = int(input('\nEnter Number of Vertices: '))
        inputMatrix = []
        for i in range(n):
            inputMatrix.append([int(j) for j in input().split()])
        inputMatrix = np.array(inputMatrix)

    else:
        inputMatrix = readMatrix('inputMatrix.txt')

    startTime = time.time()
    shortestPathsMatrix = np.array(floydWarshallSerialized(inputMatrix))
    duration = time.time() - startTime

    print(f'\nAll Pairs Shortest Paths Matrix Computed In {str(duration)} Seconds!\n')

    writeMatrix('shortestPathsMatrix.txt', shortestPathsMatrix)
