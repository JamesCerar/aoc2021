import os
import time


def importData():
    #open file, get values as list
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'input.txt')

    with open(filename, "r") as o:
        inputList = o.read().splitlines()
    
    return inputList

def getPosMapper():
    mapper = {}
    mapper[0] = {1,2,3,5,6,7}
    mapper[1] = {3,6}
    mapper[2] = {1,3,4,5,7}
    mapper[3] = {1,3,4,6,7}
    mapper[4] = {2,3,4,6}
    mapper[5] = {1,2,4,6,7}
    mapper[6] = {1,2,4,5,6,7}
    mapper[7] = {1,3,6}
    mapper[8] = {1,2,3,4,5,6,7}
    mapper[9] = {1,2,3,4,6,7}
    return mapper

def getRowMapper():
    rowMapper = {}
    for i in range(0,8):
        rowMapper[i] = {'a','b','c','d','e','f','g'}
    return rowMapper

def getSegMapper():
    segMapper = {}
    for i in ['a','b','c','d','e','f','g']:
        segMapper[i] = {1,2,3,4,5,6,7}
    return segMapper

def countLetters(wordsList):
    letterCount = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
    for i in ['a','b','c','d','e','f','g']:
        for j in wordsList:
            letterCount[i] += list(j).count(i)
    return letterCount

def updateSegMapper(segMapper,num, letter):
    for i in segMapper:
        if i == letter:
            segMapper[i] = {num}
        else:
            segMapper[i] = segMapper[i].difference({num})
    return segMapper



#Part B
start = time.time()
inputData = [i.split('|') for i in importData()]
inputValsStr = [i[0].split() for i in inputData]

inputVals = [sorted(i, key=len) for i in inputValsStr]


rowLookup = []
for row in inputVals:
    segMapper = getSegMapper()

    #get seg 6 - letter appears exactly 9 times across words
    letterCount = countLetters(row)
    seg6 = list(letterCount.keys())[list(letterCount.values()).index(9)]
    segMapper = updateSegMapper(segMapper,6,seg6)

    #get seg 2 - letter appears exactly 6 times across words
    seg2 = list(letterCount.keys())[list(letterCount.values()).index(6)]
    segMapper = updateSegMapper(segMapper,2,seg2)

    #get seg 5 - letter appears exactly 4 times across words
    seg5 = list(letterCount.keys())[list(letterCount.values()).index(4)]
    segMapper = updateSegMapper(segMapper,5,seg5)
    
    #get seg 3 - set difference of 2-lettered word (which is a 1) and seg 6
    seg3 = list(set(list(row[0])).difference(set(seg6)))[0]
    segMapper = updateSegMapper(segMapper,3,seg3)

    #get seg 1 - set difference of 3-lettered word (which is a 7) and seg3/6
    seg1 = list(set(list(row[1])).difference(set([seg6,seg3])))[0]
    segMapper = updateSegMapper(segMapper,1,seg1)

    #get seg 4 - set difference of 4-lettered word (which is a 4) and segs 2/3/6
    seg4 = list(set(list([i for i in row if len(i) == 4][0])).difference({seg2,seg3,seg6}))[0]
    segMapper = updateSegMapper(segMapper,4,seg4)

    #segmapper complete. Map to rowLookup
    for i in segMapper:
        segMapper[i] = list(segMapper[i])[0]
    rowLookup.append(segMapper)


#now do outputs
outputValsStr = [i[1].split() for i in inputData]
posMatch = getPosMapper()
totalVal = 0
for rowNum in range(0,len(outputValsStr)):
    rowOut = ''
    for word in outputValsStr[rowNum]:
        newWord = set()
        for char in word:
            newWord.add(rowLookup[rowNum][char])
        for i in posMatch:
            if posMatch[i] == newWord:
                rowOut += str(i)

    totalVal += int(rowOut)
print(totalVal)


print(time.time() - start)