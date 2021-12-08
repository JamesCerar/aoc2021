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

def getFishDict():
    return {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

def incrementFishDict(fishDict, relMap):
    newFishDict = getFishDict()
    for i in newFishDict:
        newFishDict[i] = fishDict[relMap[i]]

    newFishDict[6] += fishDict[0]
    return newFishDict

     

start = time.time()
inputData = list(map(int, importData()[0].split(',')))

relMap = {8:0, 7:8, 6:7, 5:6, 4:5, 3:4, 2:3, 1:2, 0:1}

fishDict = getFishDict() #initial fishDict

for i in fishDict: #add intial fishDict data
    fishDict[i] = inputData.count(i)

for i in range(0,256): #do 80 loops / do 256 loops
    fishDict = incrementFishDict(fishDict,relMap)

total = 0
for i in fishDict:
    total += fishDict[i]

print(total)
end = time.time()
print(end - start)