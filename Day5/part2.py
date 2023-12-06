import pathlib

input = pathlib.Path('/workspaces/adventofcode23/Day5/input.txt')
inputArray = input.read_text().split('\n\n')
inputArray = [line.split('\n') for line in inputArray]

seedList = [int(seed) for seed in inputArray[0][0].split(':')[1].split()] # Found a fancy way of reading the input courtesy of https://github.com/b-locke/aoc-23/blob/cd6032f196830b137c5f7bf760c15184d6918b7c/day-5-pt-2.py
seeds = [[seedList[i], seedList[i] + seedList[i+1]-1] for i in range(0, len(seedList), 2)]
mapList = inputArray[1:]

# Now I can go through each map and run my seeds through with range. After banging my head against the wall, using help from https://github.com/b-locke/aoc-23/blob/cd6032f196830b137c5f7bf760c15184d6918b7c/day-5-pt-2.py
for map in mapList:
    i = 0
    
    while i < len(seeds):
        if i == 10:
            print('hi')
        flag = False
        seedLeft, seedRight = seeds[i]
        for mapLine in map[1:]:
            mapLine = mapLine.split(" ")
            mapLine = [eval(i) for i in mapLine]
            if (seedLeft >= mapLine[1]) and (seedLeft < mapLine[1] + mapLine[2]) and flag == False:
                flag = True
                seeds[i][0] = mapLine[0] + (seedLeft - mapLine[1])
                if seedRight < mapLine[1] + mapLine[2]:
                    seeds[i][1] = mapLine[0] + (seedRight - mapLine[1])
                else:
                    seeds[i][1] = mapLine[0] + mapLine[2] - 1
                    seeds.append([mapLine[1] + mapLine[2], seedRight])
                    
            elif (seedRight >= mapLine[1]) and (seedRight < mapLine[1] + mapLine[2]) and flag == False:
                flag = True
                seeds[i][1] = mapLine[0] + (seedRight - mapLine[1])
                if seedLeft > mapLine[1]:
                    seeds[i][0] = mapLine[0] + (seedLeft - mapLine[1])
                else:
                    seeds[i][0] = mapLine[0]
                    seeds.append([seedLeft, mapLine[1] - 1])
        i += 1

print(min(min(seed) for seed in seeds))