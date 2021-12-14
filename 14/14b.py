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

     
#Part B - do many substitutions
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

#create dictionary with current pairs
pairsDict = defaultdict(int)
for j in range(0,len(pTemplate)-1):
    pairsDict[pTemplate[j:j+2]]+=1

#for each pair - how many times did that pair appear? Split into two new pairs, and add to new iteration
for i in range(0,iters):
    iterStart = time.time()
    print('iter '+str(i+1))
    newPairsDict = defaultdict(int)
    for j in pairsDict:
        newLet = insRules[j]
        newPairsDict[j[0]+newLet] += pairsDict[j]
        newPairsDict[newLet+j[1]] += pairsDict[j]
    pairsDict = newPairsDict.copy()
    print(time.time() - iterStart)

#count total number of letters in all pairs
elementDict = defaultdict(int)
for i in pairsDict:
    elementDict[i[0]] += pairsDict[i]
    elementDict[i[1]] += pairsDict[i]

#add one for first and last letter in template (they'll always be there, and this method doesn't capture them), and then divide by 2
firstLast = [pTemplate[0],pTemplate[-1]]
for i in elementDict:
    if i in firstLast: elementDict[i] += 1
    elementDict[i] = elementDict[i] / 2

maxVal = 0
minVal = 0
for e in elementDict:
    if maxVal == 0:
        maxVal = elementDict[e]
        minVal = elementDict[e]
    else:
        maxVal = max(maxVal,elementDict[e])
        minVal = min(minVal,elementDict[e])

print(maxVal - minVal)



print(time.time() - start)