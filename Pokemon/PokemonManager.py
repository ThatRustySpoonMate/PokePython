import os, random, Conventions, math

superEffectiveChart =   [[      "Normal", "Grass", "Fire", "Water", "Electric", "Fighting", "Ice", "Rock", "Ground", "Flying", "Poison", "Psychic", "Ghost", "Fairy", "Dark", "Steel", "Dragon", "Bug", "Typeless"],
                        ["Normal", 1,        1,       1,      1,       1,          1,          1,     0.5,    1,        1,        1,        1,         0,       1,       1,      0.5,     1,        1,       1],
                        ["Grass",  1,        0.5,     0.5,    2,       1,          1,          1,     2,      2,        0.5,      0.5,      1,         1,       1,       1,      1,       0.5,      0.5,     1],        
                        ["Fire",   1,        2,       0.5,    0.5,     1,          1,          2,     0.5,    1,        1,        1,        1,         1,       1,       1,      2,       0.5,      2,       1],
                        ["Water",  1,        0.5,     2,      0.5,     1,          1,          1,     2,      2,        1,        1,        1,         1,       1,       1,      1,       0.5,      1,       1],
                        ["Electric",1,       0.5,     1,      2,       0.5,        1,          1,     1,      0,        2,        1,        1,         1,       1,       1,      1,       0.5,      1,       1],
                        ["Fighting",2,       1,       1,      1,       1,          1,          2,     2,      1,        0.5,      0.5,      0.5,       0,       0.5,     2,      2,       1,        0.5,     1],
                        ["Ice",    1,        2,       0.5,    0.5,     1,          1,          0.5,   1,      2,        2,        1,        1,         1,       1,       1,      0.5,     2,        1,       1],
                        ["Rock",   1,        0.5,     2,      1,       1,          0.5,        2,     1,      0.5,      2,        1,        1,         1,       1,       1,      0.5,     1,        2,       1],
                        ["Ground", 1,        0.5,     2,      1,       2,          1,          1,     2,      1,        0,        2,        1,         1,       1,       1,      2,       1,        0.5,     1],
                        ["Flying", 1,        2,       1,      1,       0.5,        2,          1,     0.5,    1,        1,        1,        1,         1,       1,       1,      0.5,     1,        2,       1],
                        ["Poison", 1,        2,       1,      1,       1,          1,          1,     0.5,    0.5,      1,        0.5,      0.5,       0.5,     2,       1,      0,       1,        1,       1],
                        ["Psychic",1,        1,       1,      1,       1,          2,          1,     1,      1,        1,        2,        0.5,       1,       1,       0,      0.5,     1,        0.5,     1],
                        ["Ghost",  0,        1,       1,      1,       1,          1,          1,     1,      1,        1,        1,        2,         2,       1,       0.5,    1,       1,        1,       1],
                        ["Fairy",  1,        1,       1,      1,       1,          2,          1,     1,      1,        1,        0.5,      1,         1,       1,       2,      0.5,     2,        1,       1],
                        ["Dark",   1,        1,       1,      1,       1,          2,          1,     1,      1,        1,        1,        2,         2,       0.5,     0.5,     1,       1,        1,      1],
                        ["Steel",  1,        1,       0.5,    0.5,     0.5,        1,          2,     2,      1,        1,        1,        1,         1,       2,       1,      0.5,     1,        1,       1],
                        ["Dragon", 1,        1,       1,      1,       1,          1,          1,     1,      1,        1,        1,        1,         1,       0,       1,      0.5,     2,        1,       1],
                        ["Bug",    1,        2,       0.5,    1,       1,          0.5,        1,     1,      1,        0.5,      0.5,      2,         0.5,     0.5,     2,      0.5,     1,        1,       1],
                        ["Typeless", 1,      1,       1,      1,       1,          1,          1,     1,      1,        1,        1,        1,         1,       1,       1,      1,       1,        1,       1]
                        ]


class status:

    def __init__(self, name, master, modifyValue=33, healValue=1):
        self.name = name #Name of status effect
        self.master = master #Pokemon that this effect is applied to
        self.occurence = "after" #Before or after turn
        self.turnsLeft = 1 #Turns left before status effect goes away
        self.modifyValue = modifyValue #Value as a percentage to modify stat by
        self.healValue = healValue #Value of heal

        self.increaseFactor = round(1 + self.modifyValue / 100, 2)
        self.decreaseFactor = round(1 - self.modifyValue / 100, 2)

        if(self.name == "poison"):
            self.posionDamage = 6
            self.turnsLeft = -1
        elif(self.name == "burn"):
            self.burnDamage = math.ceil(1/16 * self.master.maxHp)
            self.turnsLeft = -1
            self.AtkTakenAway = self.master.attack * 0.25
            self.master.attack *= 0.75
        elif(self.name == "sleep"):
            self.turnsLeft = random.randrange(3, 8)
            self.occurence = "before"
        elif(self.name == "paralyze"):
            self.chanceForParalysis = 40
            self.turnsLeft = -1
            self.occurence = "before"
        elif(self.name == "freeze"):
            self.turnsLeft = -1
            self.chanceToThaw = 20
            self.occurence = "before"
        elif(self.name == "confusion"):
            self.chanceForConfusion = 33
            self.confusionDamage = 40 
            self.confusionDamageType = "Typeless"
            self.occurence = "before"
            self.turnsLeft = random.randrange(3, 8)
        elif(self.name == "flinch"):
            self.occurence = "before"
       

    def performEffect(self):
        if(self.name == "normal"):
            return
        elif(self.name == "poison"):
            self.master.hp -= self.posionDamage
            self.posionDamage += 8
            print(str(self.master.name) + " is poisoned for " + str(self.posionDamage) + ".")

        elif(self.name == "paralyze"):
            if(random.randrange(0, 100) < self.chanceForParalysis):
                self.master.noTurn = True
                print(str(self.master.name) + " is paralyzed.")

        elif(self.name == "freeze"):
            if(random.randrange(0,100) > self.chanceToThaw):
                master.noTurn = True
                print(str(self.master.name) + " is frozen solid.")
            else:
                self.master.noTurn = False
                self.turnsLeft = 1
                print(str(self.master.name) + " has thawed out.")

        elif(self.name == "burn"):
            self.master.hp =  Conventions.clamp(self.master.hp - self.burnDamage, 0, self.master.maxHp)    
            print(str(self.master.name) + " burned for " + str(self.burnDamage) + ".")

        elif(self.name == "confusion"):
            if(random.randrange(0, 100) <= self.chanceForConfusion):
                print(str(self.master.name) + " hurt himself in confusion.")
                self.master.takeDamage(self.confusionDamage, self.confusionDamageType, False)
           
        elif(self.name == "sleep"):
            if(self.turnsLeft > 1):
                self.master.noTurn = True
                print(str(self.master.name) + " is sleeping peacefully.")
            else:
                print(str(self.master.name) + " has awoken!")

        elif(self.name == "flinch"):
            print(str(self.master.name) + " has flinched and couldn't move.")
            self.master.noTurn = True

        elif(self.name == "heal"):
            print(str(self.master.name) + " has healed for " + str(self.healValue) + ".")
            self.master.hp = Conventions.clamp(self.master.hp + self.healValue, 0, self.master.maxHp)

        elif(self.name == "cure"):
            print(str(self.master.name) + " has healed all status conditions.")
            self.master.status = ["normal"]

        elif(self.name == "defDec"):
            self.master.defense = round(self.master.defense * self.decreaseFactor)
            print(str(self.master.name) + "'s defense has been decreased to " + str(self.decreaseFactor) + "x!") 
        elif(self.name == "atkDec"):
            self.master.attack = round(self.master.attack * self.decreaseFactor)
            print(str(self.master.name) + "'s attack has been decreased to " + str(self.decreaseFactor) + "x!") 
        elif(self.name == "spdDec"):
            self.master.speed = round(self.master.speed * self.decreaseFactor)
            print(str(self.master.name) + "'s speed has been decreased to " + str(self.decreaseFactor) + "x!") 
        elif(self.name == "accDec"):
            self.master.accuracy = round(self.master.accuracy * self.decreaseFactor)
            print(str(self.master.name) + "'s accuracy has been decreased to " + str(self.decreaseFactor) + "x!") 
        elif(self.name == "evaDec"):
            self.master.evasiveness = round(self.master.evasiveness * self.decreaseFactor)
            print(str(self.master.name) + "'s evasiveness has been decreased to " + str(self.decreaseFactor) + "x!") 
        elif(self.name == "defInc"):
            self.master.defense = round(self.master.defense * self.increaseFactor)
            print(str(self.master.name) + "'s defense has been increased by " + str(self.increaseFactor) + "x!") 
        elif(self.name == "atkInc"):
            self.master.attack = round(self.master.attack * self.increaseFactor)
            print(str(self.master.name) + "'s attack has been increased by " + str(self.increaseFactor) + "x!") 
        elif(self.name == "spdInc"):
            self.master.speed = round(self.master.speed * self.increaseFactor)
            print(str(self.master.name) + "'s speed has been increased by " + str(self.increaseFactor) + "x!") 
        elif(self.name == "accInc"):
            self.master.accuracy = round(self.master.accuracy * self.increaseFactor)
            print(str(self.master.name) + "'s accuracy has been increased by " + str(self.increaseFactor) + "x!") 
        elif(self.name == "evaInc"):
            self.master.evasiveness = round(self.master.evasiveness * self.increaseFactor)
            print(str(self.master.name) + "'s evasiveness has been increased by " + str(self.increaseFactor) + "x!") 

        self.decrementTurnsLeft()

    def decrementTurnsLeft(self):
        self.turnsLeft -= 1

        if(self.turnsLeft == 0):
            self.removeStatus()

    def removeStatus(self):
        if(self.name == "burn"):
            self.master.attack += self.AtkTakenAway
        if(self.name == "burn" or self.name == "freeze" or self.name == "poison" or self.name == "paralyze" or self.name == "confusion"):
           print(str(self.master.name) + "is no longer influenced by " + str(self.name))
        self.master.status.remove(self)


class pokemon:

    def __init__(self, name, Type, level, hp, speed, attack, defense, moveset, sprite = "none", noTurn = False, evasiveness=1, accuracy=1):
        self.name = name
        self.type = Type
        self.level = int(level)
        self.hp = int(hp)
        self.maxHp = int(hp)
        self.speed = int(speed)
        self.moveset = moveset
        self.evasiveness = evasiveness
        self.accuracy = accuracy
        self.status = [status("normal", self)]
        self.attack = attack
        self.defense = defense
        self.noTurn = noTurn
        self.sprite = sprite

    def isSameType(self, Type):
        if("/" in self.type):
            myType = self.type.split("/")
        else:
            myType = self.type

        if Type in myType:
            return True
        else:
            return False

    def getEffectiveness(self, Type):
        if("/" in self.type):
            myType = self.type.split("/")
        else:
            myType = self.type

        moveTypeIndex = locateTypeInChart(Type)
        if(len(myType) == 1):
            pokeTypeIndex = locateTypeInChart(myType[0])
            return superEffectiveChart[moveTypeIndex + 1][pokeTypeIndex + 1]

        elif(len(myType) == 2):
            return superEffectiveChart[moveTypeIndex + 1][locateTypeInChart(myType[0]) + 1] * superEffectiveChart[moveTypeIndex + 1][locateTypeInChart(myType[1]) + 1]

    def takeDamage(self, damageAmount, damageType, canCrit=True, statusEffect="none"):
        if(damageAmount > 0):
            if(canCrit):
                criticalChance = 10
                criticalScored = random.randrange(0, 100)
                if(criticalScored < criticalChance):
                    damageAmount *= 2
                    print("Critical Hit!")

            #Apply damage
            moveEffectiveness = self.getEffectiveness(damageType)
            if(moveEffectiveness == 2):
                print("It was super effective!")
            elif(moveEffectiveness == 0.5):
                print("It's not very effective...")

            damageAmount = round(damageAmount * moveEffectiveness)
            self.hp = Conventions.clamp(self.hp - damageAmount, 0, self.maxHp)
            print("Hit for " + str(damageAmount))

        if(statusEffect != "none"): 
            exists = False
            #Check if status already exists
            for currentStatusEffect in self.status:
                if(currentStatusEffect.name == statusEffect[4]):
                    exists = True
            if(exists == False):
                #If status effect doesnt exist on this pokemon already, create it
                newStatusEffect = status(statusEffect[4], self, statusEffect[1], statusEffect[2])
                self.status.append(newStatusEffect)
            else:
               print(str(statusEffect[4]) + " has failed.")



def getPokemonFromFile(name):
    script_dir = os.path.dirname(__file__) #<-- absolute directory the script is in
    rel_path = "Data\\Pokedata.txt"
    filePath = os.path.join(script_dir, rel_path)

    lookup = name.lower()
    lineNum = -1
    with open(filePath) as myFile:
        for num, line in enumerate(myFile, 1):
            if lookup in line.lower():
                lineNum = num

    pokedata = open(filePath, "r")
    randomFactor = round(random.uniform(0.8,1.2), 2)

    if(lineNum == -1):
        return "none"
    lines = pokedata.readlines()
    name = lines[lineNum - 1].replace("\n", "")
    Type = lines[lineNum].replace("\n", "")
    level = lines[lineNum + 1].replace("\n", "")
    hp = int(lines[lineNum + 2]) * randomFactor 
    speed = round(int(lines[lineNum + 3]) * randomFactor)
    attack = round(int(lines[lineNum + 4]) * randomFactor)
    defense = round(int(lines[lineNum + 5]) * randomFactor)
    pokedata.close()
    Type = Type.replace("\n", "")
    if("/" in Type):
        Type = Type.split("/")
    else:
        Type = [Type]

    #Generate random moves from list provided in text file
    #Determine where two "-"'s are that enclose moves
    separator1 = lineNum + 7

    pokedata = open(filePath, "r")
    currentLineNum = 0
    separator2 = 0
    for line in pokedata:
        line = line.replace("\n", "")
        currentLineNum += 1
        if(currentLineNum > separator1):
            if(line == "-"):
                separator2 = currentLineNum
                currentLineNum = -9999999

    moveRanges = separator1 + 1
    moveRange = []
    while moveRanges < separator2:
        moveRange.append(moveRanges)
        moveRanges += 1

    pickedMoves = []
    
    while len(pickedMoves) != 4:
        tempPick = random.randrange(moveRange[0] - 1, moveRange[len(moveRange) - 1])
        if(tempPick not in pickedMoves):
            pickedMoves.append(tempPick)

    move1 = lines[pickedMoves[0]].split("/")
    move2 = lines[pickedMoves[1]].split("/")
    move3 = lines[pickedMoves[2]].split("/")
    move4 = lines[pickedMoves[3]].split("/")
    move1[len(move1) - 1] = move1[len(move1) - 1].replace("\n", "")
    move2[len(move2) - 1] = move2[len(move2) - 1].replace("\n", "")
    move3[len(move3) - 1] = move3[len(move3) - 1].replace("\n", "")
    move4[len(move4) - 1] = move4[len(move4) - 1].replace("\n", "")

    move1 = embedStatusEffects(move1)
    move2 = embedStatusEffects(move2)
    move3 = embedStatusEffects(move3)
    move4 = embedStatusEffects(move4)

    moveset = []
    moveset.append(move1)
    moveset.append(move2)
    moveset.append(move3)
    moveset.append(move4)
    pokedata.close()


    return pokemon(name, Type, level, hp, speed, attack, defense, moveset)
    


def locateTypeInChart(desType):
    #desType = desType.lower()
    i = 0
    index = 0

    for Type in superEffectiveChart[0]:
        if(Type == desType):
        	index = i
        i += 1

    return index


def embedStatusEffects(move):
    moveLength = len(move)
    if(moveLength > 7):
        amountOfStatusEffects = int((moveLength -7) / 5)
        i = 0
        index = len(move) - 1
        for i in range(0, amountOfStatusEffects):
            p = 0
            index += 1
            move.append([])
            for p in range(0, 5):
                move[index].append(move.pop(7))
                index -= 1

    else:
        return move

    listLength = len(move)
    statusEffectCount = listLength - 7

    if(statusEffectCount > 0):
        move.insert(7, [])
        i = 0
        while i < statusEffectCount:
            move[7].append(move.pop(8))
            i +=1
    return move










