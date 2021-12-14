import os
import time
import re
from math import ceil

##Part A##

def importData():
    #open file, get values as list
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'input.txt')

    with open(filename, "r") as o:
        inputList = o.read().splitlines()
    
    return inputList


     
#Part B - complete the incompletes
start = time.time()

inputList = importData()
goodMatch = ['()','[]','\{\}','<>']
reverse = {'(':')','[':']','{':'}','<':'>'}
scoring = {')':1,']':2,'}':3,'>':4}
incompletes = []

score = []
for i in inputList:
    valids = True
    while valids:
        i = re.sub('\<\>|\(\)|\{\}|\[\]','',i)
        if len(i) == 0:
            valids = False
        elif re.search('\<\>|\(\)|\{\}|\[\]',i):
            valids = True
        elif not re.search('\<\>|\(\)|\{\}|\[\]',i):
            valids = False
            if not re.search('\>|\)|\}|\]',i):
                newI = ''
                for char in list(reversed(i)):
                    newI += reverse[char]
                print(newI)
                newScore = 0
                for char in list(newI):
                    newScore = newScore * 5
                    newScore += scoring[char]
                score.append(newScore)

score.sort()
middle = ceil(len(score)/2) - 1
print(score[middle])

print(time.time() - start)