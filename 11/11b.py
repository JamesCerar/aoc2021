import os
import time
import re

def importData():
    #open file, get values as list
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'input.txt')

    with open(filename, "r") as o:
        inputList = o.read().splitlines()
    
    return inputList


def updateArray(array, row, col):
    neighbours = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    numRows = len(array)
    numCols = len(array[0])
    for n in neighbours:
        if row + n[0] >= 0 and row + n[0] < numRows and col + n[1] >= 0 and col + n[1] < numCols:
            if array[row+n[0]][col+n[1]] != 0:
                array[row+n[0]][col+n[1]] += 1
            if array[row+n[0]][col+n[1]] > 9:
                array[row+n[0]][col+n[1]] = 0
                array = updateArray(array,row+n[0],col+n[1])
    return array



     
#Part B - find sync'd flashes
start = time.time()

octoMap = [list(map(int,list(x))) for x in importData()]

iters = 10000 #max number of iterations
numRows = len(octoMap)
numCols = len(octoMap[0])

for i in range(1,iters+1):
    newOctoMap = [[y+1 for y in x] for x in octoMap]
    for row in range(0,numRows):
        for col in range(0,numCols):
            if newOctoMap[row][col]>9:
                newOctoMap[row][col] = 0
                newOctoMap = updateArray(newOctoMap,row,col)

    octoMap = newOctoMap
    if sum([sum(x) for x in octoMap]) == 0:
        print('winner!')
        print(i)
        break

print(time.time() - start)