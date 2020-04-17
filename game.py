import random

places ='''GO
OLD KENT ROAD
COMMUNITY CHEST
WHITECHAPEL ROAD
INCOME TAX
KINGS CROSS STATION
THE ANGEL ISLINGTON
CHANCE
EUSTON ROAD
PENTONVILLE ROAD
JAIL
PALL MALL
ELECTRIC COMPANY
WHITEHALL
NORTHUMBERLAND AVENUE
MARYLEBONE STATION
BOW STREET
COMMUNITY CHEST
MARLBOROUGH STREET
VINE STREET
FREE PARKING
STRAND
CHANCE
FLEET STREET
TRAFALGAR SQUARE
FENCHURCH ST. STATION
LEICESTER SQUARE
COVENTRY STREET
WATER WORKS
PICCADILLY
GO TO JAIL
REGENT STREET
OXFORD STREET
COMMUNITY CHEST
BOND STREET
LIVERPOOL ST. STATION
CHANCE
PARK LANE
SUPER TAX
MAYFAIR'''.split("\n")

chances='''mon
_GO
_MAYFAIR
_PALL MALL
_TRAFALGAR SQUARE
mon
jailFree
-3
_JAIL
mon
mon
mon
_MARYLEBONE STATION
mon
mon
mon'''.split("\n")

communityChests='''_GO
mon
mon
mon
mon
jailFree
_OLD KENT ROAD
_JAIL
mon
mon
mon
mon
mon
mon
mon
mon'''.split("\n")


def rollDice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return str(dice1+dice2)+','+str(int(dice1==dice2))

landedSpaces = [0]*len(places)

def game():
    random.shuffle(chances)
    random.shuffle(communityChests)
    playLoc = 0
    chanceLoc = 0
    commLoc = 0
    card = " "
    doubleStreak = 0
    for i in range(100):
        #print(places[playLoc])
        if (places[playLoc] == "CHANCE"):
            card = chances[chanceLoc]
            chanceLoc+=1
            if chanceLoc-len(chances) >=0:
                chanceLoc-=len(chances)
            #print(card)
        
        if (places[playLoc] == "COMMUNITY CHEST"):
            card = communityChests[commLoc]
            commLoc+=1
            if commLoc-len(communityChests) >=0:
                commLoc-=len(communityChests)
            #print(card)

        if (card[0] == "_"):
            playLoc = places.index(card[1:])
            #print(places[playLoc])
            card = " "
        if (card[0] == "-"):
            playLoc -= int(card[1:])
            #print(places[playLoc])
            card = " "
        if (places[playLoc] == "GO TO JAIL"):
            playLoc = 10
        
        landedSpaces[playLoc]+=1
        
        #input()
        
        functionOut = rollDice()
        diceRoll = int(functionOut.split(',')[0])
        double = bool(int(functionOut.split(',')[1]))

        #print(diceRoll)
        if(double):
            #print("It was a double")
            doubleStreak += 1
            #print("Double Streak: "+str(doubleStreak))
        else:
            doubleStreak = 0

        if(doubleStreak >= 3):
            playLoc=10
        else:
            playLoc+= diceRoll
        
        if(playLoc-len(places)>=0):
            playLoc-=len(places)

def displayLanded(landedSpaces):
    for space in range(len(landedSpaces)):
        print(str(places[space])+','+str(round(landedSpaces[space]/sum(landedSpaces),4)))

for i in range(100000):
    game()

displayLanded(landedSpaces)
