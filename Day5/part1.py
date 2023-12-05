input = open('/workspaces/adventofcode23/Day5/input.txt')
inputArray = input.readlines()
print(inputArray)
newSection = True
map = []
for line in inputArray:   
    line = line.removesuffix("\n")
    if line == "":
        seedPlaceholderList = []
        if  map:
            for seed in seeds:
                newSeed = seed
                for mapLine in map:
                    if (seed >= mapLine[1]) and (seed < mapLine[1] + mapLine[2]):
                        # Seed falls within the mapping, need to convert.
                        newSeed = (seed - mapLine[1]) + mapLine[0]
                seedPlaceholderList.append(newSeed)
                                          
            map = []
            seeds = seedPlaceholderList
        newSection = True
    elif "seeds: " in line:
        newSection = False
        seeds = line.removeprefix("seeds: ").split(" ")
        seeds = [int(numeric_string) for numeric_string in seeds]
    
    elif newSection:
        if "map:" in line:
            continue
        else:
            #Start doing some mapping
            lineArray = line.split(" ")
            lineArray = [int(numeric_string) for numeric_string in lineArray]
            map.append(lineArray)






print(min(seeds))