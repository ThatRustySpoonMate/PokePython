import random, math

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




x = False
def pr():
	global x
	x = True

#pr()
#print(x)


def locateTypeInChart(desType):
    desType = desType.lower()
    i = 0
    index = 0

    for Type in superEffectiveChart[0]:
        if(Type.lower() == desType):
            index = i
        i += 1

    return index

#print(locateTypeInChart("Dark"))
#print("thunder wave".replace(" ", ""))


print((12-7)/5)