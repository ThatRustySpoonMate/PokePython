import struct
icons = [["normal", "grass", "fire", "electric", "water"], [" ", "🍂", "🔥", "⚡", "💧"]]

def getTypeIcon(Type):
    if(len(Type) == 1):
        Type = Type[0].lower()
        try:
            index = icons[0].index(Type)
            return icons[1][index]
        except:
       	    return ""
    elif(len(Type) == 2):
    	stub = 0 #Work on this
    else:
    	return ""


    	

