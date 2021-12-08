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


     
#Part A
start = time.time()
partA = [2,4,3,7]

inputData = [i.split('|') for i in importData()]
outputValsStr = [i[1].split() for i in inputData]
counter = 0
for i in outputValsStr:
    for j in i:
        if len(j) in partA: counter+=1


print(counter)

print(time.time() - start)