input = open('/workspaces/adventofcode23/Day4/input.txt')
inputArray = input.readlines()
print(inputArray)

class Card:
    def __init__(self, line):
        self.id = int(line.split(':')[0].removeprefix('Card ').removesuffix(':'))
        self.winningNumbers = line.split(':')[1].split(' | ')[0].split(' ')
        self.winningNumbers = [i for i in self.winningNumbers if i] # Remove blanks
        self.myNumbers = line.split(':')[1].split(' | ')[1].split(' ')
        self.myNumbers = [i for i in self.myNumbers if i] # Remove blanks
    
    def returnMatches(self):
        matches = [value for value in self.winningNumbers if value in self.myNumbers]
        return matches


cardDict = {}
cards = []
for line in inputArray:
    line = line.removesuffix('\n')
    cards.append(Card(line))
    cardDict[Card(line).id] = 1
score = 0


for card in cards:
    #print(len(card.returnMatches()))
    if len(card.returnMatches()) > 0:
        score = len(card.returnMatches())
        i = 0
        while score > 0:
            cardDict[card.id + score] += cardDict[card.id]
            score = score - 1
result = 0
for item in cardDict.values():
    result += item

print(result)