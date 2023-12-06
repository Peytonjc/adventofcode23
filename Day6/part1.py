input = open('/workspaces/adventofcode23/Day6/input.txt')
inputArray = input.readlines()
print(inputArray)

timeList = inputArray[0].removeprefix("Time:").removesuffix('\n').split(' ')
timeList = [i for i in timeList if i]
timeList = [int(numeric_string) for numeric_string in timeList]
distList = inputArray[1].removeprefix("Distance:").removesuffix('\n').split(' ')
distList = [i for i in distList if i]
distList = [int(numeric_string) for numeric_string in distList]

i = 0
winningList = []
while i < len(timeList):
    winNum = 0
    j = 1
    time = timeList[i]
    while j < time:
        calcDist = j*(time - j)
        if calcDist > distList[i]:
            winNum += 1
        j += 1
    winningList.append(winNum)
    i += 1

result = 1
for num in winningList:
    result = num * result

print(result)