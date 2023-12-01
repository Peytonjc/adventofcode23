

input = open('/workspaces/adventofcode23/Day1/input1.txt')
inputArray = input.readlines()
print(inputArray)
num1 = 'Z'
num2 = 'Z'
sum = 0
for line in inputArray:
    line = line.replace('one', 'o1e')
    line = line.replace('two', 't2o')
    line = line.replace('three', 'th3ee')
    line = line.replace('four', 'f4ur')
    line = line.replace('five', 'f5ve')
    line = line.replace('six', 's6x')
    line = line.replace('seven', 'se7en')
    line = line.replace('eight', 'ei8ht')
    line = line.replace('nine', 'n9ne')
    line = line.replace('zero', 'z0ro')
    for char in line:
        if char.isnumeric() :
            if num1 == 'Z':
                num1 = char
            else:
                num2 = char

    if num2 == 'Z':
        num2 = num1    
    sum += int(str(num1) + str(num2))
    num1 = 'Z'
    num2 = 'Z'
print(sum)

