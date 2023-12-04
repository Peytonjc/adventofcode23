input = open('/workspaces/adventofcode23/Day2/input1.txt')
inputArray = input.readlines()
print(inputArray)

possibleDict = {'red': 12, 'green': 13, 'blue': 14}
result = 0

for line in inputArray:
    goodGame = True
    gameID = int(line.split(':')[0].removeprefix('Game ').removesuffix(':'))
    gameArray = line.split(':')[1].split('; ')
    maxRed = 0
    maxBlue = 0
    maxGreen = 0
    for cycle in gameArray:
        cycle = cycle.removesuffix('\n')
        colors = cycle.split(',')
        for colorline in colors:
            colorline = colorline.removeprefix(' ')
            number = int(colorline.split(' ')[0])
            colorType = colorline.split(' ')[1]
            if number > possibleDict[colorType]:
                goodGame = False
            match colorType:
                case 'red':
                    #Need to add match-case statements to check against the max variables. then find the power at the end of each game

    if goodGame:
        result += gameID
    print(gameID)
print(result)