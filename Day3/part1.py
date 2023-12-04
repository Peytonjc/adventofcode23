input = open('/workspaces/adventofcode23/Day3/input.txt')
inputArray = input.readlines()
print(inputArray)

result = 0
numberDict = []
# First, lets find all the numbers and store their row/column nums. Also find symbols
row = 0
numberHolder = ''
numberLocations = []
symbolLocations = []
for line in inputArray:
    line = line.removesuffix('\n')
    index = 0
    while index < len(line):
        if line[index].isnumeric():
            numberHolder += (line[index])
            numberLocations.append(index)
        elif line[index] != '.':
            if line[index - 1].isnumeric():
                numberDict.append([numberHolder, row, numberLocations, False])
                numberHolder = ''
                numberLocations = []
            symbolLocations.append([row, index])
        elif len(numberLocations) > 0:
            numberDict.append([numberHolder, row, numberLocations, False])
            numberHolder = ''
            numberLocations = []
        index += 1
    if len(numberLocations) > 0:
            numberDict.append([numberHolder, row, numberLocations, False])
            numberHolder = ''
            numberLocations = []
    row += 1

# Convert the symbol locations to valid locations for numbers
validLocations = []
for symbolLocation in symbolLocations:
    validLocations.append([symbolLocation[0] - 1, symbolLocation[1] - 1])
    validLocations.append([symbolLocation[0] - 1, symbolLocation[1]])
    validLocations.append([symbolLocation[0] - 1, symbolLocation[1] + 1])
    validLocations.append([symbolLocation[0], symbolLocation[1] - 1])
    validLocations.append([symbolLocation[0], symbolLocation[1] + 1])
    validLocations.append([symbolLocation[0] + 1, symbolLocation[1] - 1])
    validLocations.append([symbolLocation[0] + 1, symbolLocation[1]])
    validLocations.append([symbolLocation[0] + 1, symbolLocation[1] + 1])

i = 0    
while i < len(numberDict):
    for val in numberDict[i][2]:
        if [numberDict[i][1], val] in validLocations:
            numberDict[i][3] = True
    i += 1

j = 0
while j < len(numberDict):
    if numberDict[j][3]:
        result += int(numberDict[j][0])
    else:
        print(numberDict[j][0])
    j += 1
#Works for the test input... gotta debug...

print(result)