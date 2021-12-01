import os

##Part A##

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')


with open(filename, "r") as o:
    inputList = list(map(int, o.readlines()))

increasedVals = 0
for i in range(1,len(inputList)):
    if inputList[i] > inputList[i-1]:
        increasedVals += 1

print(increasedVals)

increasedVals = 0
for i in range(3,len(inputList)):
    if inputList[i] + inputList[i-1] + inputList[i-2] > inputList[i-1] + inputList[i-2] + inputList[i-3]:
        increasedVals += 1

print(increasedVals)