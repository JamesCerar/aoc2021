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

def makeBasin(array,row,col,n):
    neighbours = [[-1,0],[0,-1],[0,1],[1,0]]
    n.add((row,col))
    for i in neighbours:
        newRow, newCol = row + i[0], col + i[1]
        if (newRow,newCol) not in n and array[newRow][newCol] == '0':
            newN = makeBasin(array,newRow,newCol,n)
            n = n.union(newN)
    return n


     
#Part B - find basins
start = time.time()

inputList = importData()

#adding buffer rows and columns to top/bottom/sides
numRows = len(inputList) + 2
numCols = len(inputList[0]) + 2
bufferRow = '.' * numCols

bufferedMap = []
bufferedMap.append(bufferRow)
for row in inputList:
    for i in range(0,9):
        row = row.replace(str(i),'0')
    bufferedMap.append('.'+row.replace('9','.')+'.')
bufferedMap.append(bufferRow)


#make basin map
allBasins = []
alphaNum = 0
for rowNum in range(0,numRows):
    for colNum in range(0,numCols):
        if bufferedMap[rowNum][colNum] == '0':
            alphaNum+=1
            curLetter = chr(ord('a')+alphaNum%24-1)
            newBasin = makeBasin(bufferedMap,rowNum,colNum,set())
            allBasins.append(len(newBasin))
            for i in newBasin:
                bufferedMap[i[0]] = bufferedMap[i[0]][:i[1]] + curLetter + bufferedMap[i[0]][i[1]+1:]
                


#create list of basin sizes
allBasins.sort(reverse=True)

for i in bufferedMap:
    print(i)

print(allBasins[0]*allBasins[1]*allBasins[2])
print(time.time() - start)