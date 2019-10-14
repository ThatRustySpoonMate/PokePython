import os, random

def getPokemonFromFile(name):
	script_dir = os.path.dirname(__file__).replace("Libraries", "") #<-- absolute directory the script is in
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


print(getPokemonFromFile)