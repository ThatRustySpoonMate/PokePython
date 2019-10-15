import os, time, random, traceback, tkinter as tk #Python built-in modules
import Icon, Conventions, PokemonManager as pm #My own modules 
#from playsound import playsound
from PIL import ImageTk, Image
from pygame import mixer 


script_dir = os.path.dirname(__file__) #<-- absolute directory the script is in

rel_path = "AudioFiles"
audioFolder = os.path.join(script_dir, rel_path)
rel_path = "PokeSprites"
spriteFolder = os.path.join(script_dir, rel_path)
battleMusic = "\\Attack_On_Titan.mp3"

os.system('cls')

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
        
 
def turn(turnData):
    os.system('cls')
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

    #For move set array
    aName = 0
    aDamage = 1
    aAccuracy = 2
    aPP = 3
    aPriority = 4
    aType = 5
    aCanCrit = 6
    aStatusArray = 7

    aStatus1 = 0

    #For status within move set array
    aStatusChance = 0
    aDebuffMod = 1
    aStatusAmount = 2
    aTarget = 3
    aStatusEffect = 4

    #Run each status condition that affects the user before their turn
    for statusEffect in turnData[aFirst][aPokemon].status:
        if(statusEffect.occurence == "before"):
            statusEffect.performEffect()

    if(turnData[aFirst][aPokemon].noTurn == False):
        #Announce used move
        print(turnData[aFirst][aTrainer].name + "'s " + str(turnData[aFirst][aPokemon].name) + " used " + str(turnData[aFirst][aMove][aName]))
        
        #for the sake of efficiency, calculate accuracy first
        if(turnData[aFirst][aMove][aAccuracy] == 100 or random.randrange(0,100) <= int(turnData[aFirst][aMove][aAccuracy]) * (int(turnData[aFirst][aPokemon].accuracy) / int(turnData[aSecond][aPokemon].evasiveness) ) ):
            #Get base damage of move
            damage = int(turnData[aFirst][aMove][aDamage])
            #Determine if same-type-attack, if so, 50% more damage
            if(turnData[aFirst][aPokemon].isSameType(str(turnData[aFirst][aMove][aType]))):
                damage = int(round(damage * 1.5))

            #calculate damage to opponent
            attackMultiplier =  1 + ((turnData[aFirst][aPokemon].attack - turnData[aSecond][aPokemon].defense) / 300)
            damage = round(damage * attackMultiplier)


            #Apply damage 
            turnData[aSecond][aPokemon].takeDamage(damage, turnData[aFirst][aMove][aType], turnData[aFirst][aMove][aCanCrit]) 

            #Status effect
            if(len(turnData[aFirst][aMove]) >= 8):
                for effect in turnData[aFirst][aMove][aStatusArray]:
                    effect[aStatusChance] = int(effect[aStatusChance])
                    effect[aStatusAmount] = int(effect[aStatusAmount])
                    effect[aDebuffMod] = int(effect[aDebuffMod])
                    #Loop through each effect
                    statusEffective = random.randrange(0, 100)
                    #Determine chance of effect happening
                    if(statusEffective <= effect[aStatusChance]):
                        #If status effect hit, determine which pokemon it applies to (user or opposer)
                        if(effect[aTarget] == "other"):
                            #Hits Opposer
                            turnData[aSecond][aPokemon].takeDamage(0, "Typeless", False, effect)
                        elif(effect[aTarget] == "self"):
                            #Hits user
                            turnData[aFirst][aPokemon].takeDamage(0, "Typeless", False, effect)

        #If move missed, announce to user
        else:
            print(turnData[aFirst][aMove][aName] +  " has missed")

        #Getting index of used move
        moveIndexTemp = 0
        for move in turnData[aFirst][aTrainer].activePokemon.moveset:
            if(move == turnData[aFirst][aMove]):
                moveindex = moveIndexTemp
            moveIndexTemp += 1
        #Decrementing pp - Using move index
        turnData[aFirst][aTrainer].activePokemon.moveset[moveindex][3] = int(turnData[aFirst][aTrainer].activePokemon.moveset[moveindex][3]) - 1
                

    #Run each status condition that affects the user before their turn
    for statusEffect in turnData[aSecond][aPokemon].status:
        if(statusEffect.occurence == "before"):
            statusEffect.performEffect()

    if(turnData[aSecond][aPokemon].noTurn == False):
        #Announce used move
        print(turnData[aSecond][aTrainer].name + "'s " + str(turnData[aSecond][aPokemon].name) + " used " + str(turnData[aSecond][aMove][aName]))
        
        #for the sake of efficiency, calculate accuracy first
        if(turnData[aSecond][aMove][aAccuracy] == 100 or random.randrange(0,100) <= int(turnData[aSecond][aMove][aAccuracy]) * (int(turnData[aSecond][aPokemon].accuracy) / int(turnData[aSecond][aPokemon].evasiveness) ) ):
            #Get base damage of move
            damage = int(turnData[aSecond][aMove][aDamage])
            #Determine if same-type-attack, if so, 50% more damage
            if(turnData[aSecond][aPokemon].isSameType(str(turnData[aSecond][aMove][aType]))):
                damage = int(round(damage * 1.5))

            #calculate damage to opponent
            attackMultiplier =  1 + ((turnData[aSecond][aPokemon].attack - turnData[aFirst][aPokemon].defense) / 300)
            damage = round(damage * attackMultiplier)


            #Apply damage 
            turnData[aFirst][aPokemon].takeDamage(damage, turnData[aSecond][aMove][aType], turnData[aSecond][aMove][aCanCrit]) 

            #Status effect
            if(len(turnData[aSecond][aMove]) >= 8):
                for effect in turnData[aSecond][aMove][aStatusArray]:
                    effect[aStatusChance] = int(effect[aStatusChance])
                    effect[aStatusAmount] = int(effect[aStatusAmount])
                    effect[aDebuffMod] = int(effect[aDebuffMod])
                    #Loop through each effect
                    statusEffective = random.randrange(0, 100)
                    #Determine chance of effect happening
                    if(statusEffective <= effect[aStatusChance]):
                        #If status effect hit, determine which pokemon it applies to (user or opposer)
                        if(effect[aTarget] == "other"):
                            #Hits Opposer
                            turnData[aFirst][aPokemon].takeDamage(0, "Typeless", False, effect)
                        elif(effect[aTarget] == "self"):
                            #Hits user
                            turnData[aSecond][aPokemon].takeDamage(0, "Typeless", False, effect)

        #If move missed, announce to user
        else:
            print(turnData[aSecond][aMove][aName] +  " has missed")

        #Getting index of used move
        moveIndexTemp = 0
        for move in turnData[aSecond][aTrainer].activePokemon.moveset:
            if(move == turnData[aSecond][aMove]):
                moveindex = moveIndexTemp
            moveIndexTemp += 1
        #Decrementing pp - Using move index
        turnData[aSecond][aTrainer].activePokemon.moveset[moveindex][3] = int(turnData[aSecond][aTrainer].activePokemon.moveset[moveindex][3]) - 1

        print("")
        #Run each status condition that affects the user after their turn
        for statusEffect in turnData[aFirst][aPokemon].status:
            if(statusEffect.occurence == "after"):
                statusEffect.performEffect()

        #Run each status condition that affects the user after their turn
        for statusEffect in turnData[aSecond][aPokemon].status:
            if(statusEffect.occurence == "after"):
                statusEffect.performEffect()



    
    #Lastly, empty all variables and update windows

    Trainer1.activePokemon.noTurn = False
    Trainer2.activePokemon.noTurn = False
    trainer1MoveSelected = False
    trainer2MoveSelected = False
    trainer1Data = []
    trainer2Data = []
    Player1Window.updateWindow()
    Player1Window.app.updateWindow()


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

    #Check if all moves are locked in
    if(trainer1MoveSelected == True and trainer2MoveSelected == True):
    	#Check priorities first
        if(int(trainer1Data[1][4]) > int(trainer2Data[1][4])):
            turnData = [trainer1Data, trainer2Data]
        elif(int(trainer2Data[1][4]) > int(trainer1Data[1][4])):
            turnData = [trainer2Data, trainer1Data]
        #If priorities of moves are equal, compare speed of pokemon
        elif(Trainer1.activePokemon.speed > Trainer2.activePokemon.speed):
            turnData = [trainer1Data, trainer2Data]
        elif(Trainer2.activePokemon.speed > Trainer1.activePokemon.speed):
            turnData = [trainer2Data, trainer1Data]
        #If priorities are equal, flip a coin to determine who moves first
        elif(Trainer1.activePokemon.speed == Trainer2.activePokemon.speed):
            coinFlip = random.randrange(1,3)
            if(coinFlip == 1):
                turnData = [trainer1Data, trainer2Data]
            else:
                turnData = [trainer2Data, trainer1Data]

        turn(turnData)
        turnData = []


trainer1MoveSelected = False
trainer2MoveSelected = False
trainer1Data = []
trainer2Data = []
turnData = []




class Trainer1ControlWindow:
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

        self.PokemonDescription = tk.Text(self.frame, height = 10, width = 20)
        self.PokemonDescription.configure(state = tk.DISABLED)


        self.buttonPlayer1Move1.grid(column = 0, row = 2)
        self.buttonPlayer1Move2.grid(column = 0, row = 3)
        self.PokeSprite.grid(column = 1, row = 1)
        #self.EnemySprite.grid(column = 3, row = 1)
        self.buttonPlayer1Move3.grid(column = 4, row = 2)
        self.buttonPlayer1Move4.grid(column = 4, row = 3)
        self.buttonPlayer1Switch.grid(column = 2, row = 0)
        self.Title.grid(column = 0, row = 0)
        self.Title.insert(tk.END, Trainer1.name)

        self.PokemonDescription.grid(column = 4, row = 0)
        try:
            self.updateWindow()
        except Exception:
            traceback.print_exc()

        self.frame.pack()


    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Trainer2ControlWindow(self.newWindow)


    def updateWindow(self):
        #Hide normal status conditions when others are present
        #Updating active pokemon info
        self.PokemonDescription.configure(state = tk.NORMAL)
        self.PokemonDescription.delete(1.0, tk.END)
        #Determine status conditions to display
        statusText = ""
        if(len(Trainer1.activePokemon.status) == 1):
            statusText = Trainer1.activePokemon.status[0].name
        else:
            statuses = Trainer1.activePokemon.status[1:]
            for status in statuses:
                statusText += (status.name + ", ")

        #Determine pokemon types to display
        if(len(Trainer1.activePokemon.type) == 1):
            pokeTypeText = Trainer1.activePokemon.type[0]
        else:
            pokeTypeText = Trainer1.activePokemon.type[0] + "/" + Trainer1.activePokemon.type[1] 


        updatedText = str(Trainer1.activePokemon.name) + "\n\n" + pokeTypeText + "\nHP: " + str(Trainer1.activePokemon.hp) + "/" + str(Trainer1.activePokemon.maxHp) + "\nLVL: " + str(Trainer1.activePokemon.level) + "\nSpeed: " + str(Trainer1.activePokemon.speed) + "\nAtk: " + str(Trainer1.activePokemon.attack) + "\nDef: " + str(Trainer1.activePokemon.defense) + "\nStatus: " + statusText 
        self.PokemonDescription.insert(tk.END, updatedText)
        self.PokemonDescription.configure(state = tk.DISABLED)

        #Updating move-set and PP for active pokemon and disable moves that dont have any pp left
        if(int(Trainer1.activePokemon.moveset[0][3]) > 0):
            self.buttonPlayer1Move1.configure(text = Trainer1.activePokemon.moveset[0][0] + "\n(" + str(Trainer1.activePokemon.moveset[0][3]) + ")")
        else:
            self.buttonPlayer1Move1.configure(state = tk.DISABLED)

        if(int(Trainer1.activePokemon.moveset[1][3]) > 0):
            self.buttonPlayer1Move2.configure(text = Trainer1.activePokemon.moveset[1][0] + "\n(" + str(Trainer1.activePokemon.moveset[1][3]) + ")")
        else:
            self.buttonPlayer1Move2.configure(state = tk.DISABLED)

        if(int(Trainer1.activePokemon.moveset[2][3]) > 0):
            self.buttonPlayer1Move3.configure(text = Trainer1.activePokemon.moveset[2][0] + "\n(" + str(Trainer1.activePokemon.moveset[2][3]) + ")")
        else:
            self.buttonPlayer1Move3.configure(state = tk.DISABLED)

        if(int(Trainer1.activePokemon.moveset[3][3]) > 0):
            self.buttonPlayer1Move4.configure(text = Trainer1.activePokemon.moveset[3][0] + "\n(" + str(Trainer1.activePokemon.moveset[3][3]) + ")")
        else:
            self.buttonPlayer1Move4.configure(state = tk.DISABLED)





class Trainer2ControlWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.buttonPlayer2Move1 = tk.Button(self.frame, text = Trainer2.activePokemon.moveset[0][0] + "\n(" + str(Trainer2.activePokemon.moveset[0][3]) + ")", width = 25, command = lambda:movePressed(Trainer2, Trainer2.activePokemon.moveset[0]))
        self.buttonPlayer2Move2 = tk.Button(self.frame, text = Trainer2.activePokemon.moveset[1][0] + "\n(" + str(Trainer2.activePokemon.moveset[1][3]) + ")", width = 25, command = lambda:movePressed(Trainer2, Trainer2.activePokemon.moveset[1]))
        self.buttonPlayer2Move3 = tk.Button(self.frame, text = Trainer2.activePokemon.moveset[2][0] + "\n(" + str(Trainer2.activePokemon.moveset[2][3]) + ")", width = 25, command = lambda:movePressed(Trainer2, Trainer2.activePokemon.moveset[2]))
        self.buttonPlayer2Move4 = tk.Button(self.frame, text = Trainer2.activePokemon.moveset[3][0] + "\n(" + str(Trainer2.activePokemon.moveset[3][3]) + ")", width = 25, command = lambda:movePressed(Trainer2, Trainer2.activePokemon.moveset[3]))
        self.buttonPlayer2Switch = tk.Button(self.frame, text = 'Switch', width = 25)
      
        self.Title = tk.Text(self.frame, height = 1, width = len(Trainer2.name))
        self.PokemonDescription = tk.Text(self.frame, height = 10, width = 20)
        self.PokemonDescription.configure(state = tk.DISABLED)

        self.buttonPlayer2Move1.grid(column = 0, row = 2)
        self.buttonPlayer2Move2.grid(column = 0, row = 3)
        self.buttonPlayer2Move3.grid(column = 4, row = 2)
        self.buttonPlayer2Move4.grid(column = 4, row = 3)
        self.buttonPlayer2Switch.grid(column = 2, row = 0)
        self.Title.grid(column = 0, row = 0)
        self.Title.insert(tk.END, Trainer2.name)

        self.PokemonDescription.grid(column = 4, row = 0)
        try:
            self.updateWindow()
        except Exception:
        	traceback.print_exc()

        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


    def updateWindow(self):
        #Updating active pokemon info - Change display of pokemon type to string rather than array, accounting for bi-typed pokemon
        self.PokemonDescription.configure(state = tk.NORMAL)
        self.PokemonDescription.delete(1.0, tk.END)

        statusText = ""
        #Determine status conditions to display
        if(len(Trainer2.activePokemon.status) == 1):
            statusText = Trainer2.activePokemon.status[0].name
        else:
            statuses = Trainer2.activePokemon.status[1:]
            for status in statuses:
                statusText += (status.name + ", ")

        #Determine pokemon types to display
        if(len(Trainer2.activePokemon.type) == 1):
            pokeTypeText = Trainer2.activePokemon.type[0]
        else:
        	pokeTypeText = Trainer2.activePokemon.type[0] + "/" + Trainer2.activePokemon.type[1] 
        updatedText = str(Trainer2.activePokemon.name) + "\n\n" + pokeTypeText + "\nHP: " + str(Trainer2.activePokemon.hp) + "/" + str(Trainer2.activePokemon.maxHp) + "\nLVL: " + str(Trainer2.activePokemon.level) + "\nSpeed: " + str(Trainer2.activePokemon.speed) + "\nAtk: " + str(Trainer2.activePokemon.attack) + "\nDef: " + str(Trainer2.activePokemon.defense) + "\nStatus: " + statusText 
        self.PokemonDescription.insert(tk.END, updatedText)
        self.PokemonDescription.configure(state = tk.DISABLED)

        #Updating move-set and PP for active pokemon 

        if(int(Trainer2.activePokemon.moveset[0][3]) > 0):
            self.buttonPlayer2Move1.configure(text = Trainer2.activePokemon.moveset[0][0] + "\n(" + str(Trainer2.activePokemon.moveset[0][3]) + ")")
        else:
            self.buttonPlayer2Move1.configure(state = tk.DISABLED)
        
        if(int(Trainer2.activePokemon.moveset[1][3]) > 0):
            self.buttonPlayer2Move2.configure(text = Trainer2.activePokemon.moveset[1][0] + "\n(" + str(Trainer2.activePokemon.moveset[1][3]) + ")")
        else:
            self.buttonPlayer2Move2.configure(state = tk.DISABLED)
        
        if(int(Trainer2.activePokemon.moveset[2][3]) > 0):
            self.buttonPlayer2Move3.configure(text = Trainer2.activePokemon.moveset[2][0] + "\n(" + str(Trainer2.activePokemon.moveset[2][3]) + ")")
        else:
            self.buttonPlayer2Move3.configure(state = tk.DISABLED)
        
        if(int(Trainer2.activePokemon.moveset[3][3]) > 0):
            self.buttonPlayer2Move4.configure(text = Trainer2.activePokemon.moveset[3][0] + "\n(" + str(Trainer2.activePokemon.moveset[3][3]) + ")")
        else:
            self.buttonPlayer2Move4.configure(state = tk.DISABLED)



#TEST DATA
#try:
#	POKE1 = pm.getPokemonFromFile("Flowdart")
#except Exception:
#	traceback.print_exc()

#POKE2 = pm.getPokemonFromFile("Chrisodon")
#POKE3 = pm.getPokemonFromFile("Pikachu")
#Trainer1 = trainer("Ethan", [POKE1, POKE2, POKE3], POKE1)
#input(Trainer1.activePokemon.getEffectiveness("Water"))
#input(Trainer1.checkAllLife())

greeting = ["Hewwo", "Mornin'", "Evenin'", "Howdy", "Top of the morning", "Whats poppin'", "What's cooking", "Sup,", "I'm pretty fly for a white guy"]
reference = ["young lad,", "old mate,", "lass,", "mate,", "kiddo,", "bucko,", "chap,", ""]
ending = ["what be thy name?", "what do you call yourself?", "what do you want me to call ya?", "what's yerr name?"]
name1 = input("Prof. Willmington - '" + greeting[random.randrange(-1, len(greeting) - 1)] + " " + reference[random.randrange(-1, len(reference) - 1)] + " " + ending[random.randrange(-1, len(ending) - 1)] + "'\n")

time.sleep(4)
name2 = input("And while we're at it " + name1 + ", who are you challenging on this fine day?\n")
time.sleep(1)

os.system('cls')

print("Prof. Willmington - 'I'll give you two a control window each after you both pick your pokemon, that's when the real fun begins.'")

time.sleep(2)

preference = random.randrange(1,3)
preferenceName = name1
if(preference == 1):
    preferenceName = name1
if(preference == 2):
    preferenceName = name2

sly = ["my money is on " + preferenceName, "it's obvious " + preferenceName + " is going to win", preferenceName + " is going to take the dub this game."]
print("Alright, well " + sly[random.randrange(-1, len(sly) - 1)] + ".")
time.sleep(2)
os.system("cls")
print("------------------------" + name1.upper() + "'S POKEMON SELECTION------------------------")
partySize = 0
validPartySize = ["1","2","3","4","5","6"] 
while partySize not in validPartySize:
    partySize = input("How many pokemon in the party? (1-6)\n")
partySize = int(partySize)

Trainer1SelectedPokemon = []

while(len(Trainer1SelectedPokemon) != partySize):
    tempPokemon = input(str(len(Trainer1SelectedPokemon) + 1) + ") Pokemon name: ")
    if(pm.getPokemonFromFile(tempPokemon) != "none"):
        Trainer1SelectedPokemon.append(pm.getPokemonFromFile(tempPokemon))
    else:
        print("Please check your spelling.")
    time.sleep(1.5)


os.system("cls")
print("------------------------" + name2.upper() + "'S POKEMON SELECTION------------------------")
Trainer2SelectedPokemon = []

while(len(Trainer2SelectedPokemon) != partySize):
    tempPokemon = input(str(len(Trainer2SelectedPokemon) + 1) + ") Pokemon name: ")
    if(pm.getPokemonFromFile(tempPokemon) != "none"):
        Trainer2SelectedPokemon.append(pm.getPokemonFromFile(tempPokemon))
    else:
        print("Please check your spelling.")
    time.sleep(1.5)

#POKEMON ARE SELECTED
os.system("cls")

Trainer1 = trainer(name1, Trainer1SelectedPokemon, Trainer1SelectedPokemon[0])
Trainer2 = trainer(name2, Trainer2SelectedPokemon, Trainer2SelectedPokemon[0]) 

root = tk.Tk()

Player1Window = Trainer1ControlWindow(root) 

mixer.init()
mixer.music.load(audioFolder + battleMusic)
mixer.music.play(20)

root.title("Control")
Player1Window.new_window()
root.resizable(False, False)
root.mainloop()

#Insert pokemonSprite = getSprite()

#Combat sequence
trainerOrder = [0, 0]

#while(Trainer1.checkAllLife() == True and Trainer2.checkAllLife() == True):
	#Determine who moves first 


	#Work on function for handling attacks 
