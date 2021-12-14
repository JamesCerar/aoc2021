import os
import time


def importData(dummy=False):
    #open file, get values as list
    filenameDict = {True:'input_dummy.txt',False:'input.txt'}
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, filenameDict[dummy])

    with open(filename, "r") as o:
        inputList = o.read().splitlines()
    
    return inputList


def makeFold(coordList,axis,loc):
    newCoordList = []
    if axis == 'x':
        axisInd = 0
    else:
        axisInd = 1

    for coord in coordList:
        constVal = coord[1-axisInd]
        varVal = coord[axisInd]
        if varVal < loc:
            newCoordList.append(coord)
        elif varVal > loc:
            newVarVal = loc - (varVal - loc)
            newCoord = [0,0]
            newCoord[1-axisInd] = constVal
            newCoord[axisInd] = newVarVal
            if newCoord not in coordList: newCoordList.append(newCoord)

    return newCoordList

def printChart(coordList):
    maxX = max([i[0] for i in coordList]) + 1
    maxY = max([i[1] for i in coordList]) + 1
    newRow = '.'*maxX
    chart = []
    for i in range(0,maxY):
        chart.append(newRow)
    
    for coord in coordList:
        chart[coord[1]] = chart[coord[1]][:coord[0]] + '#' + chart[coord[1]][coord[0]+1:]
    
    for i in chart:
        print(i)


     
#Part A - do first fold
start = time.time()

inputList = importData()

isInput = True
coordList = []
foldList = []
for i in inputList:
    if i == '':
        isInput = False
    elif isInput:
        coordList.append(list(map(int,list(i.split(',')))))
    else:
        fold = list(i.replace('fold along ','').split('='))
        foldList.append([fold[0],int(fold[1])])


for inst in foldList:
    coordList = makeFold(coordList,inst[0],inst[1])

printChart(coordList)




print(time.time() - start)