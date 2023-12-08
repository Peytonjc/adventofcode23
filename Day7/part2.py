input = open('/workspaces/adventofcode23/Day7/input.txt')
inputArray = input.readlines()
print(inputArray)

class hand:
    def __init__(self, line):
        self.value = int(line.split(' ')[1])
        # 7 - Five of a kind, 6 - Four of a kind, 5 - Full house, 4 - Three of a kind, 3 - Two pair, 2 - One pair, 1 - None
        self.handLine = line.split(' ')[0]
        self.handValueList = []
        count = 0
        for char in self.handLine:
            if self.handLine.count(char) > count:
                count = self.handLine.count(char)
            if char.isnumeric():
                self.handValueList.append(int(char))
            else:
                match char:
                    case 'A':
                        self.handValueList.append(13)
                    case 'K':
                        self.handValueList.append(12)
                    case 'Q':
                        self.handValueList.append(11)
                    case 'J':
                        self.handValueList.append(1)
                    case 'T':
                        self.handValueList.append(10)
        if 'J' not in self.handLine:
            if count == 5:
                self.type = 7
            elif count == 4:
                self.type = 6
            elif count == 3:
                # determine if it is full house or three of a kind
                if len(set(self.handLine)) == 2:
                    self.type = 5
                else:
                    self.type = 4
            elif count == 2:
                # determine if it is two or one pair
                if len(set(self.handLine)) == 3:
                    self.type = 3
                else:
                    self.type =2
            else:
                self.type = 1
        else:
            jCount = self.handLine.count('J')
            if count == 5:
                self.type = 7
            elif count == 4:
                if jCount == 1:
                    # ex KKKKJ
                    self.type = 7
                else:
                    # ex JJJJK five of a kind
                    self.type = 7
            elif count == 3:
                # determine if it is full house or three of a kind
                if len(set(self.handLine)) == 2:
                    # ex. JJ222 five of a kind
                    self.type = 7
                else:
                    if jCount == 1:
                        # ex. J3222 four of a kind
                        self.type = 6
                    else:
                        # ex. 23JJJ four of a kind
                        self.type = 6
            elif count == 2:
                # determin if it is two or one pair
                if len(set(self.handLine)) == 3:
                    if jCount == 1:
                        # ex. J2233 full house
                        self.type = 5
                    elif jCount == 2: 
                        #ex. JJ233 four of a kind
                        self.type = 6
                else:
                    if jCount == 1:
                        # ex. J2344 three of a kind
                        self.type = 4
                    elif jCount == 2:
                        # ex. JJ234 three of a kind
                        self.type = 4
            else:
                self.type = 2


handList = []
for line in inputArray:
    line = line.removesuffix('\n')
    handList.append(hand(line))

handList.sort(key=lambda x: (x.type, x.handValueList[0], x.handValueList[1], x.handValueList[2], x.handValueList[3], x.handValueList[4]), reverse=True)

x = len(handList)
i = 0
result = 0
while x > 0:
    result += (x * handList[i].value)
    x = x - 1
    i += 1

print(result)