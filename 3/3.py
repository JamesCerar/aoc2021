import os
import time

##Part A##

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')


with open(filename, "r") as o:
    inputList = o.read().splitlines()


#Part A
start = time.time()
totalNums = len(inputList)
sumBits = {1:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
for i in inputList:
    for n in range(0,len(i)):
        sumBits[n+1] += int(i[n])

gamma = ''
epsilon = ''

for i in sumBits:
    if sumBits[i] > totalNums/2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma,2)*int(epsilon,2))
print(time.time() - start)

#Part B
start = time.time()

oxrList = inputList
cosList = inputList

oxr = ''
for i in range(0,len(inputList[0])):
    countDigit = sum([int(j[i]) for j in oxrList])
    totalNum = len(oxrList)
    if countDigit >= totalNum / 2: 
        oxr += '1'
    else:
        oxr += '0'
    newOxrList = []
    for row in oxrList:
        if row[0:i+1] == oxr:
            newOxrList.append(row)
    oxrList = newOxrList
    if len(oxrList) == 1: break

cos = ''
for i in range(0,len(inputList[0])):
    countDigit = sum([int(j[i]) for j in cosList])
    totalNum = len(cosList)
    if countDigit < totalNum / 2: 
        cos += '1'
    else:
        cos += '0'
    newCosList = []
    for row in cosList:
        if row[0:i+1] == cos:
            newCosList.append(row)
    cosList = newCosList
    if len(cosList) == 1: break


print(int(oxrList[0],2))
print(int(cosList[0],2))

print(int(cosList[0],2) * int(oxrList[0],2))



print(time.time() - start)