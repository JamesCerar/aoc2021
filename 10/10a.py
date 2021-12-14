import os
import time
import re

##Part A##

def importData():
    #open file, get values as list
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'input.txt')

    with open(filename, "r") as o:
        inputList = o.read().splitlines()
    
    return inputList


     
#Part A - find invalids
start = time.time()

inputList = importData()
goodMatch = ['()','[]','\{\}','<>']
scoring = {']':57,')':3,'}':1197,'>':25137}
invalids = []

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
            if re.search('\>|\)|\}|\]',i):
                #invalidIndex = re.search('\>|\)|\}|\]',i).start()
                #invalids.append(i[invalidIndex-2:invalidIndex-1])
                invalids.append(re.findall('\>|\)|\}|\]',i)[0])

totalScore = sum([scoring[i] for i in invalids])

print(invalids)
print(totalScore)



print(time.time() - start)