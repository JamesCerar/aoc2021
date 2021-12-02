import os

##Part A##

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')


with open(filename, "r") as o:
    inputList = list(map(str, o.readlines()))

up = 0
forward = 0
for row in inputList:
    keyVal = row.split()
    if keyVal[0] == 'down':
        up -= int(keyVal[1])
    elif keyVal[0] == 'up':
        up += int(keyVal[1])
    elif keyVal[0] == 'forward':
        forward += int(keyVal[1])

print(up)
print(forward)

aim = 0
up = 0
forward = 0
for row in inputList:
    keyVal = row.split()
    if keyVal[0] == 'down':
        aim += int(keyVal[1])
    elif keyVal[0] == 'up':
        aim -= int(keyVal[1])
    elif keyVal[0] == 'forward':
        forward += int(keyVal[1])
        up += aim * int(keyVal[1])

print(up)
print(forward)
