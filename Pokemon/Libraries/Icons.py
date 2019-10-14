
icons = [["normal", "grass", "fire", "electric", "water"], [" ", "🍂", "🔥", "⚡", "💧"]]

def getTypeIcon(Type):
    Type = Type.lower()
    try:
        index = icons[0].index(Type)
    except:
        return ""
    return icons[1][index]


