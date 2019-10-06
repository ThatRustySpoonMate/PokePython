import os, time, random
import tkinter as tk
from playsound import playsound
from PIL import ImageTk, Image

superEffectiveChart =   [[      "Normal", "Grass", "Fire", "Water", "Electric", "Fighting", "Ice", "Rock", "Ground", "Flying", "Poison", "Psychic", "Ghost", "Fairy", "Dark", "Steel", "Dragon", "Bug"],
						["Normal", 1,        1,       1,      1,       1,          1,          1,     0.5,    1,        1,        1,        1,         0,       1,       1,      0.5,     1,        1],
						["Grass",  1,        0.5,     0.5,    2,       1,          1,          1,     2,      2,        0.5,      0.5,      1,         1,       1,       1,      1,       0.5,      0.5],        
						["Fire",   1,        2,       0.5,    0.5,     1,          1,          2,     0.5,    1,        1,        1,        1,         1,       1,       1,      2,       0.5,      2],
						["Water",  1,        0.5,     2,      0.5,     1,          1,          1,     2,      2,        1,        1,        1,         1,       1,       1,      1,       0.5,      1],
						["Electric",1,       0.5,     1,      2,       0.5,        1,          1,     1,      0,        2,        1,        1,         1,       1,       1,      1,       0.5,      1],
						["Fighting",2,       1,       1,      1,       1,          1,          2,     2,      1,        0.5,      0.5,      0.5,       0,       0.5,     2,      2,       1,        0.5],
						["Ice",    1,        2,       0.5,    0.5,     1,          1,          0.5,   1,      2,        2,        1,        1,         1,       1,       1,      0.5,     2,        1],
						["Rock",   1,        0.5,     2,      1,       1,          0.5,        2,     1,      0.5,      2,        1,        1,         1,       1,       1,      0.5,     1,        2],
						["Ground", 1,        0.5,     2,      1,       2,          1,          1,     2,      1,        0,        2,        1,         1,       1,       1,      2,       1,        0.5],
						["Flying", 1,        2,       1,      1,       0.5,        2,          1,     0.5,    1,        1,        1,        1,         1,       1,       1,      0.5,     1,        2],
						["Poison", 1,        2,       1,      1,       1,          1,          1,     0.5,    0.5,      1,        0.5,      0.5,       0.5,     2,       1,      0,       1,        1],
						["Psychic",1,        1,       1,      1,       1,          2,          1,     1,      1,        1,        2,        0.5,       1,       1,       0,      0.5,     1,        0.5],
						["Ghost",  0,        1,       1,      1,       1,          1,          1,     1,      1,        1,        1,        2,         2,       1,       0.5,    1,       1,        1],
						["Fairy",  1,        1,       1,      1,       1,          2,          1,     1,      1,        1,        0.5,      1,         1,       1,       2,      0.5,     2,        1],
						["Dark",   1,        1,       1,      1,       1,          2,          1,     1,      1,        1,        1,        2,         2,       0.5,     0.5,     1,       1,        1],
						["Steel",  1,        1,       0.5,    0.5,     0.5,        1,          2,     2,      1,        1,        1,        1,         1,       2,       1,      0.5,     1,        1],
						["Dragon", 1,        1,       1,      1,       1,          1,          1,     1,      1,        1,        1,        1,         1,       0,       1,      0.5,     2,        1],
						["Bug",    1,        2,       0.5,    1,       1,          0.5,        1,     1,      1,        0.5,      0.5,      2,         0.5,     0.5,     2,      0.5,     1,        1]
						]

script_dir = os.path.dirname(__file__) #<-- absolute directory the script is in

rel_path = "AudioFiles"
audioFolder = os.path.join(script_dir, rel_path)
rel_path = "PokeSprites"
spriteFolder = os.path.join(script_dir, rel_path)
battleMusic = "\\Attack_On_Titan.mp3"



class trainer:
	def __init__(self, name, party, activePokemon):
		self.name = name
		self.party = party
		self.activePokemon = activePokemon

	def SwitchPokemon(self, newPokemon):
		self.activePokemon = newPokemon
		self.activePokemon.noTurn = True

	def isAlive(self, pokemon):
		if(pokemon.hp > 0):
			return True
		else:
			return False

	def checkAllLife(self):
		allAlive = True
		aliveCounter = 0
		for pokemon in self.party:
			if(self.isAlive(pokemon)):
				aliveCounter += 1

		if(aliveCounter == 0):
			allAlive = False
		return allAlive

def getSprite(): #Name
	script_dir = os.path.dirname(__file__) #<-- absolute directory the script is in
	rel_path = "PokeSprites\\Flowdart.png"
	abs_file_path = os.path.join(script_dir, rel_path)
	sprite = ImageTk.PhotoImage(Image.open(abs_file_path))
	return sprite

class pokemon:

	def __init__(self, name, Type, level, hp, speed, moveset, sprite = "none", status = "normal", attack = 1, defense = 1, noTurn = False):
		self.name = name
		self.type = Type
		self.level = int(level)
		self.hp = int(hp)
		self.speed = speed
		self.moveset = moveset
		self.status = status
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


			


def getPokemonFromFile(name):
	script_dir = os.path.dirname(__file__) #<-- absolute directory the script is in
	rel_path = "Pokedata.txt"
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
	speed = int(lines[lineNum + 3]) * randomFactor
	pokedata.close()
	Type = Type.replace("\n", "")
	if("/" in Type):
		Type = Type.split("/")
	else:
		Type = [Type]

	#Generate random moves from list provided in text file
	#Determine where two "-"'s are that enclose moves
	separator1 = lineNum + 5

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
	move1[4] = move1[4].replace("\n", "")
	move2[4] = move2[4].replace("\n", "")
	move3[4] = move3[4].replace("\n", "")
	move4[4] = move4[4].replace("\n", "")
	moveset = []
	moveset.append(move1)
	moveset.append(move2)
	moveset.append(move3)
	moveset.append(move4)
	pokedata.close()

	return pokemon(name, Type, level, hp, speed, moveset)
	
 
def turn(turnData):
    #Turn data = [0] = Pokemon object | [1] = Move | [2] = Trainer object
    global trainer1MoveSelected
    global trainer2MoveSelected
    global trainer1Data
    global trainer2Data

    #For primary array
    aFirst = 0
    aSecond = 1

    #For turnData scope array
    aPokemon = 0
    aMove = 1
    aTrainer = 2

    #for move set array
    aName = 0
    aDamage = 1
    aAccuracy = 2
    aPP = 3
    aType = 4

    #ANNOUNCE
    print(turnData[aFirst][aTrainer].name + "'s " + str(turnData[aFirst][aPokemon].name) + " used " + str(turnData[aFirst][aMove][aName]))
    
    #EXECUTE

    #Getting index of used move
    #moveIndexTemp = 0
    #for move in Trainer1.activePokemon.moveset:
    #    if(move == trainer1Data[1]):
    #        moveindex = moveIndexTemp
    #    moveIndexTemp += 1

    #for the sake of efficiency, calculate accuracy first
    if(turnData[aFirst][aMove][aAccuracy] == 100 or random.randrange(0,100) <= int(turnData[aFirst][aMove][aAccuracy])):


        #Calculate damage to opponent
        baseDamage = int(turnData[aFirst][aMove][aDamage]) #Damage
        #Determine if stab, if so, 50% more damage
        if(turnData[aFirst][aPokemon].isSameType(str(turnData[aFirst][aMove][aType]))):
       	#Is stab
        	baseDamage = int(round(baseDamage * 1.5))

        print("Hit for " + str(baseDamage))

    #If move missed, announce to user
    else:
        print(turnData[aFirst][aMove][aName] +  " has missed")




    #Decrementing pp - Use move index
    Trainer1.activePokemon.moveset[0][3] = int(Trainer1.activePokemon.moveset[0][3]) - 1

    


    #Trainer 2's pokemon moves last
    print(turnData[aSecond][aTrainer].name + "'s " + str(turnData[aSecond][aPokemon].name) + " used " + str(turnData[aSecond][aMove][aName]))
	
	

    Trainer1.activePokemon.noTurn = False
    Trainer2.activePokemon.noTurn = False
    trainer1MoveSelected = False
    trainer2MoveSelected = False
    trainer1Data = []
    trainer2Data = []
	


def movePressed(Trainer, move):
	#print(Trainer.name + " used " + move[0])
	global trainer1MoveSelected
	global trainer2MoveSelected
	global trainer1Data
	global trainer2Data
	global turnData

	if(Trainer == Trainer1):
		trainer1MoveSelected = True
		trainer1Data = [Trainer1.activePokemon, move, Trainer1]
	if(Trainer == Trainer2):
		trainer2MoveSelected = True
		trainer2Data = [Trainer2.activePokemon, move, Trainer2]

	if(trainer1MoveSelected == True and trainer2MoveSelected == True):
		if(Trainer1.activePokemon.speed > Trainer2.activePokemon.speed):
			turnData = [trainer1Data, trainer2Data]
			#trainer1Data.append(1)
			#trainer2Data.append(2)
		else:
			turnData = [trainer2Data, trainer1Data]
			#trainer2Data.append(1)
			#trainer1Data.append(2)

		
		turn(turnData)
		turndata = []



#def switchPokemon()
	

trainer1MoveSelected = False
trainer2MoveSelected = False
trainer1Data = []
trainer2Data = []
turnData = []




class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.buttonPlayer1Move1 = tk.Button(self.frame, text = Trainer1.activePokemon.moveset[0][0] + "\n(" + str(Trainer1.activePokemon.moveset[0][3]) + ")", width = 25, command = lambda:movePressed(Trainer1, Trainer1.activePokemon.moveset[0]))
        self.buttonPlayer1Move2 = tk.Button(self.frame, text = Trainer1.activePokemon.moveset[1][0] + "\n(" + str(Trainer1.activePokemon.moveset[1][3]) + ")", width = 25, command = lambda:movePressed(Trainer1, Trainer1.activePokemon.moveset[1]))
        self.buttonPlayer1Move3 = tk.Button(self.frame, text = Trainer1.activePokemon.moveset[2][0] + "\n(" + str(Trainer1.activePokemon.moveset[2][3]) + ")", width = 25, command = lambda:movePressed(Trainer1, Trainer1.activePokemon.moveset[2]))
        self.buttonPlayer1Move4 = tk.Button(self.frame, text = Trainer1.activePokemon.moveset[3][0] + "\n(" + str(Trainer1.activePokemon.moveset[3][3]) + ")", width = 25, command = lambda:movePressed(Trainer1, Trainer1.activePokemon.moveset[3]))
        self.buttonPlayer1Switch = tk.Button(self.frame, text = "Switch", width = 25)

        self.PokeSprite = tk.Label(self.frame )#image = Trainer1.activePokemon.sprite)
        self.Title = tk.Text(self.frame, height = 1, width = len(Trainer1.name))
        #self.EnemySprite = tk.Label(self.frame, image = Trainer2.activePokemon.sprite)

        self.buttonPlayer1Move1.grid(column = 0, row = 2)
        self.buttonPlayer1Move2.grid(column = 0, row = 3)
        self.PokeSprite.grid(column = 1, row = 1)
        #self.EnemySprite.grid(column = 3, row = 1)
        self.buttonPlayer1Move3.grid(column = 4, row = 2)
        self.buttonPlayer1Move4.grid(column = 4, row = 3)
        self.buttonPlayer1Switch.grid(column = 2, row = 0)
        self.Title.grid(column = 0, row = 0)
        self.Title.insert(tk.END, Trainer1.name)

        self.frame.pack()


    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.buttonPlayer2Move1 = tk.Button(self.frame, text = Trainer2.activePokemon.moveset[0][0], width = 25, command = lambda:movePressed(Trainer2, Trainer2.activePokemon.moveset[0]))
        self.buttonPlayer2Move2 = tk.Button(self.frame, text = Trainer2.activePokemon.moveset[1][0], width = 25, command = lambda:movePressed(Trainer2, Trainer2.activePokemon.moveset[1]))
        self.buttonPlayer2Move3 = tk.Button(self.frame, text = Trainer2.activePokemon.moveset[2][0], width = 25, command = lambda:movePressed(Trainer2, Trainer2.activePokemon.moveset[2]))
        self.buttonPlayer2Move4 = tk.Button(self.frame, text = Trainer2.activePokemon.moveset[3][0], width = 25, command = lambda:movePressed(Trainer2, Trainer2.activePokemon.moveset[3]))
        self.buttonPlayer2Switch = tk.Button(self.frame, text = 'Switch', width = 25)
      
        self.Title = tk.Text(self.frame, height = 1, width = len(Trainer2.name))


        self.buttonPlayer2Move1.grid(column = 0, row = 2)
        self.buttonPlayer2Move2.grid(column = 0, row = 3)
        self.buttonPlayer2Move3.grid(column = 4, row = 2)
        self.buttonPlayer2Move4.grid(column = 4, row = 3)
        self.buttonPlayer2Switch.grid(column = 2, row = 0)
        self.Title.grid(column = 0, row = 0)
        self.Title.insert(tk.END, Trainer2.name)

        self.frame.pack()

    def close_windows(self):
        self.master.destroy()



#TEST DATA
#POKE1 = getPokemonFromFile("Flowdart")
#POKE2 = getPokemonFromFile("Chrisodon")
#POKE3 = getPokemonFromFile("Pikachu")
#Trainer1 = trainer("Ethan", [POKE1, POKE2, POKE3], POKE1)
#input(Trainer1.checkAllLife())

greeting = ["Hewwo", "Mornin'", "Evenin'", "Howdy", "Top of the morning", "Whats poppin'", "What's cooking", "Sup,", "I'm pretty fly for a white guy"]
reference = ["young lad,", "old mate,", "lass,", "mate,", "kiddo,", "bucko,", "chap,", ""]
ending = ["what be thy name?", "what do you call yourself?", "what do you want me to call ya?", "what's yerr name?"]
name1 = input("Prof. Willmington - '" + greeting[random.randrange(-1, len(greeting) - 1)] + " " + reference[random.randrange(-1, len(reference) - 1)] + " " + ending[random.randrange(-1, len(ending) - 1)] + "'\n")
time.sleep(1.2)

print("Prof. Willmington - 'Well here is your control window " + name1 + ", use it to control your pokemon in battle.'")

time.sleep(4)
name2 = input("And while we're at it " + name1 + ", who are you challenging on this fine day?\n")
time.sleep(1)

os.system('cls')
print("I should probably give you a control window too hey? Here you go:")


time.sleep(2)

preference = random.randrange(1,3)
preferenceName = name1
if(preference == 1):
	preferenceName = name1
if(preference == 2):
	preferenceName = name2

sly = ["My money is on " + preferenceName, "It's obvious " + preferenceName + " is going to win", preferenceName + " is going to take the dub this game."]
print("Alright, well " + sly[random.randrange(-1, len(sly) - 1)] + ".")
time.sleep(2)
os.system("cls")
print("------------------------" + name1.upper() + "'S POKEMON SELECTION------------------------")
partySize = int(input("How many pokemon in the party? (1-6)\n"))
Trainer1SelectedPokemon = []

while(len(Trainer1SelectedPokemon) != partySize):
	tempPokemon = input(str(len(Trainer1SelectedPokemon) + 1) + ") Pokemon name: ")
	if(getPokemonFromFile(tempPokemon) != "none"):
		Trainer1SelectedPokemon.append(getPokemonFromFile(tempPokemon))
	else:
		print("Please check your spelling.")
	time.sleep(1.5)


os.system("cls")
print("------------------------" + name2.upper() + "'S POKEMON SELECTION------------------------")
Trainer2SelectedPokemon = []

while(len(Trainer2SelectedPokemon) != partySize):
	tempPokemon = input(str(len(Trainer2SelectedPokemon) + 1) + ") Pokemon name: ")
	if(getPokemonFromFile(tempPokemon) != "none"):
		Trainer2SelectedPokemon.append(getPokemonFromFile(tempPokemon))
	else:
		print("Please check your spelling.")
	time.sleep(1.5)

#POKEMON ARE SELECTED
os.system("cls")

Trainer1 = trainer(name1, Trainer1SelectedPokemon, Trainer1SelectedPokemon[0])
Trainer2 = trainer(name2, Trainer2SelectedPokemon, Trainer2SelectedPokemon[0]) 

root = tk.Tk()

Player1Window = Demo1(root) 

root.title("Control")
Player1Window.new_window()
root.resizable(False, False)
root.mainloop()

#Insert pokemonSprite = getSprite()

#Combat sequence
trainerOrder = [0, 0]
#playsound(audioFolder + battleMusic, True)
#while(Trainer1.checkAllLife() == True and Trainer2.checkAllLife() == True):
	#Determine who moves first 


	#Work on function for handling attacks 
