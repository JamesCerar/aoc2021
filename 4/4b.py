import os
from typing import Match
import math


#open file, get values as list
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')

with open(filename, "r") as o:
    inputList = o.read().splitlines()

numsList = []
for i in inputList[0].split(','):
    numsList.append(int(i))

boardsList = inputList[2:]

#split puzzle input into boards
boards = []
newBoard = []
for i in boardsList:
    if i == '':
        boards.append(newBoard)
        newBoard = []
    else:
        newBoard.append(i.split())
boards.append(newBoard) #get last board too

#big list of wins
allWins = []

for b in boards:
    possibleWins = []

    #rows
    for r in b:
        newWin = set()
        for i in range(0,5):
            newWin.add(int(r[i]))
        possibleWins.append(newWin)
    
    #columns
    for i in range(0,5):
        newWin = set()
        for r in b:
            newWin.add(int(r[i]))
        possibleWins.append(newWin)
    
    # #diagonal - top left->bottom right
    # newWin = set()
    # for i in range(0,5):
    #     newWin.add(int(b[i][i]))
    # possibleWins.append(newWin)

    # #diagonal - top right->bottom left
    # newWin = set()
    # for i in range(0,5):
    #     newWin.add(int(b[i][4-i]))
    # possibleWins.append(newWin)

    #add board's wins to big list
    allWins.append(possibleWins)



#Part B:
#Find last winning board
allBoards = list(range(0,len(allWins)))
winningNums = set()
removedBoards = []
losingBoard = set()

for i in numsList:
    winningNums.add(i)
    for b in allBoards:
        for r in range(0,len(allWins[b])):
            allWins[b][r] = allWins[b][r].difference(winningNums)
            if len(allWins[b][r]) == 0:
                if b not in removedBoards: removedBoards.append(b)
    allBoards = list(set(allBoards).difference(set(removedBoards)))
    if len(allBoards) == 0:
        winningNum = i
        lastBoard = allWins[removedBoards[-1]]
        print(lastBoard)
        break

remainingNums = set()
for b in lastBoard:
    remainingNums = remainingNums.union(b)

sumRemaining = sum(list(remainingNums))
print(winningNum)
print(sumRemaining)
