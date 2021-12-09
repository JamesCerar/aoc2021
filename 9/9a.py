import os
import time

##Part A##

def importData():
    #open file, get values as list
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'input.txt')

    with open(filename, "r") as o:
        inputList = o.read().splitlines()
    
    return inputList


     
#Part A - find low points
start = time.time()

inputList = importData()

#adding buffer rows and columns to top/bottom/sides
numRows = len(inputList) + 2
numCols = len(inputList[0]) + 2
bufferRow = '9' * numCols

bufferedMap = []
bufferedMap.append(bufferRow)
for row in inputList:
    bufferedMap.append('9'+row+'9')
bufferedMap.append(bufferRow)

#now do calc - if value is lower than all surrounding, add to list
neighbours = [[-1,0],[0,-1],[0,1],[1,0]]
lowNums = []
for rowNum in range(1,numRows-1):
    for colNum in range(1,numCols-1):
        curNum = int(bufferedMap[rowNum][colNum])
        minNbr = 9
        for n in neighbours:
            minNbr = min(int(bufferedMap[rowNum + n[0]][colNum + n[1]]), minNbr)
        if curNum < minNbr:
            lowNums.append(curNum)

riskNumber = 0
for i in lowNums:
    riskNumber += (i + 1)

print(lowNums) 
print(riskNumber)

print(time.time() - start)