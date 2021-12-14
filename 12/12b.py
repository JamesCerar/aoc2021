import os
import time
from collections import defaultdict


def importData(dummy=False):
    #open file, get values as list
    filenameDict = {True:'input_dummy.txt',False:'input.txt'}
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, filenameDict[dummy])

    with open(filename, "r") as o:
        inputList = o.read().splitlines()
    
    return inputList

def countPrevs(curPath):
    prevDict = defaultdict(int)
    for i in curPath:
        if i.islower():
            prevDict[i] += 1
            if prevDict[i] > 1:
                return False

    return True


def getPaths(pathDict,curPath):
    #what's the current letter being done?
    curStep = curPath[-1]
    paths = []

    #what are the possible next steps? Create a new path with next steps
    for i in pathDict[curStep]:
        newPath = curPath.copy()
        if i == 'end':
            newPath.append(i)
            paths.append(newPath)
        elif i.isupper() or i not in curPath or (i not in ['start','end'] and countPrevs(curPath)):
            newPath.append(i)
            for p in getPaths(pathDict, newPath):
                paths.append(p)

    return paths

     
#Part B - count paths with one extra small
start = time.time()

inputList = [i.split('-') for i in importData()]


#create path dictionary - keys = current location, values list = connected locations
pathDict = defaultdict(list)
for i in inputList:
    pathDict[i[0]].append(i[1])
    pathDict[i[1]].append(i[0])
pathDict['end'] = []


#create paths
notAllEnds = True
paths = [['start']]
for i in paths:
    paths = getPaths(pathDict,['start'])



print(len(paths))

print(time.time() - start)