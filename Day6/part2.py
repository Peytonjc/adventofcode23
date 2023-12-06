input = open('/workspaces/adventofcode23/Day6/input.txt')
inputArray = input.readlines()
print(inputArray)

timeList = inputArray[0].removeprefix("Time:").removesuffix('\n').split(' ')
timeList = [i for i in timeList if i]
time = ''.join(timeList)
time = int(time)
#timeList = [int(numeric_string) for numeric_string in timeList]
distList = inputArray[1].removeprefix("Distance:").removesuffix('\n').split(' ')
distList = [i for i in distList if i]
dist = ''.join(distList)
dist = int(dist)
#distList = [int(numeric_string) for numeric_string in distList]

winningList = []
winNum = 0
j = 1
time = time
while j < time:
    calcDist = j*(time - j)
    if calcDist > dist:
        winNum += 1
    j += 1
winningList.append(winNum)


result = 1
for num in winningList:
    result = num * result

print(result)