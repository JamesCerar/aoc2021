import os
from typing import Match
import numpy as np

##Part A##

def importData():
    #open file, get values as list
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'input.txt')

    with open(filename, "r") as o:
        inputList = o.read().splitlines()
    
    return inputList



def addLines(x1,x2,y1,y2,array):
    #plot lines on array:

    #x lines
    if y1==y2:
        minX,maxX = min(x1,x2), max(x1,x2)
        for n in range(minX,maxX+1):
            array[n,y1] += 1
    #y lines
    elif x1==x2:
        minY,maxY = min(y1,y2), max(y1,y2)
        for n in range(minY,maxY+1):
            array[x1,n] += 1
    
    #diagonal lines
    else:
        xDir, yDir = np.sign(x2 - x1), np.sign(y2 - y1)
        len = max(x1,x2) - min(x1,x2) + 1
        for n in range(0,len):
            array[x1 + (n*xDir), y1 + (n*yDir)] += 1

    
    print(array)
    return array



inputList = importData()
lineList = []
for i in inputList:
    newRow = []
    for j in i.split(' -> '):
        newRow.append(list(map(int,j.split(','))))
    lineList.append(newRow)


#find outer bounds of array
maxX, maxY = 0,0
for i in lineList:
    for j in i:
        maxX = max(j[0],maxX)
        maxY = max(j[1],maxY)


#create 2d array of max width/length
lineArray = np.zeros([maxX+1,maxY+1])

for i in lineList:
    lineArray = addLines(i[0][0],i[1][0],i[0][1],i[1][1], lineArray)

print(lineArray)
intersections = lineArray > 1
print(intersections.sum())