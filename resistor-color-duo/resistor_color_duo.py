COLORS = ["black", "brown", "red", "orange", "yellow", 
          "green", "blue", "violet", "grey", "white"]

def value(colors):
    color1, color2, *rest = colors
    resistance = str(COLORS.index(color1)) + str(COLORS.index(color2))
    return int(resistance)