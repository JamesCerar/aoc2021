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

     
#Part A - do substitutions
start = time.time()

inputList = importData()

isInput = True
insRules = {}
for i in inputList:
    if i == '':
        isInput = False
    elif isInput:
        pTemplate = i
    else:
        rule = i.split(' -> ')
        insRules[rule[0]] = rule[1]


iters = 40
for i in range(0,iters):
    iterStart = time.time()
    print('iter '+str(i+1))
    newTemplate = ''
    for j in range(0,len(pTemplate)):
        newTemplate += pTemplate[j]
        newTemplate += insRules.get(pTemplate[j:j+2],'')
    pTemplate = newTemplate
    print(time.time() - iterStart)

elementDict = defaultdict(int)
for i in list(pTemplate):
    elementDict[i] += 1

maxVal = 0
minVal = 9999999
for e in elementDict:
    maxVal = max(maxVal,elementDict[e])
    minVal = min(minVal,elementDict[e])

print(maxVal - minVal)



print(time.time() - start)