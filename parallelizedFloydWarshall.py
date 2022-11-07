from mpi4py import MPI
import numpy as np
import time
import sys

def readMatrix(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    matrix = []

    for row in lines:
        matrix.append([int(j) for j in row.split()])

    file.close()
    return np.array(matrix)

if __name__ == "__main__":
    worldcomm = MPI.COMM_WORLD

    inputMatrix = readMatrix('inputMatrix.txt')
    shortestPathsMatrix = readMatrix('outputMatrix.txt')

    n = len(inputMatrix)
    rowsPerThread = n // worldcomm.Get_size()
    threadsPerThread = worldcomm.Get_size() / n
    startRow = rowsPerThread * worldcomm.Get_rank()
    endRow = rowsPerThread * (worldcomm.Get_rank() + 1)

    startTime = time.time()

    for k in range(n):
        inputMatrix[k] = worldcomm.bcast(inputMatrix[k], root = int(threadsPerThread * k))
        for i in range(startRow, endRow):
            for j in range(n):
                inputMatrix[i][j] = min(inputMatrix[i][j], inputMatrix[i][k] + inputMatrix[k][j])

    if worldcomm.Get_rank() == 0:
        for k in range(endRow, n):
            processRank = int((worldcomm.Get_size() / n) * k)
            inputMatrix[k] = worldcomm.recv(source = processRank, tag = 42)

        for i in range(n):
            for j in range(n):
                input = inputMatrix[i][j]
                solved = shortestPathsMatrix[i][j]

                if input != solved:
                    sys.exit(f'Mismatch At ({str(i)}, {str(j)})')

        duration = time.time() - startTime
        print(f'\nAll Pairs Shortest Paths Matrix Computed In {str(duration)} Seconds!\n')

    else:
        for k in range(startRow, endRow):
            worldcomm.send(inputMatrix[k], dest=0, tag=42)
