import os
import time

##Part A##

def importData():
    #open file, get values as list
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'input.txt')

    with open(filename, "r") as o:
        inputList = o.read().splitlines()
    
    return list(map(int, inputList[0].split(',')))

def sumFuel(start,end):
    fuelUsed = 0
    for k in range(0, abs(end-start)):
        fuelUsed += k
    
    return fuelUsed

     
#Part A
start = time.time()


inputData = importData()

i = max(inputData)
minVal = [0,1000000]
for j in range(0,i):
    fuelUsed = 0
    for k in inputData:
        fuelUsed += abs(k - j)
    if fuelUsed < minVal[1]:
        minVal[0] = j
        minVal[1] = fuelUsed

print(minVal)

print(time.time() - start)

#Part B
start = time.time()


inputData = importData()

i = max(inputData)
minVal = [0,1000000000000]
for j in range(0,i):
    fuelUsed = 0
    for k in inputData:
        n = abs(k - j)
        fuelUsed += n * (n+1) / 2

    if fuelUsed < minVal[1]:
        minVal[0] = j
        minVal[1] = fuelUsed

print(minVal)

print(time.time() - start)