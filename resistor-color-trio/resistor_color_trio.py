COLORS = ["black", "brown", "red", "orange", "yellow", 
          "green", "blue", "violet", "grey", "white"]


def label(colors):
    color1, color2, zeros, *rest = colors
    resistance = str(COLORS.index(color1)) + str(COLORS.index(color2))
    resistance = int(resistance) * 10 ** COLORS.index(zeros)

    if resistance > 10**9:
        resistance = str(resistance // 10**9) + " gigaohms"
    elif resistance > 10**6:
        resistance = str(resistance // 10**6) + " megaohms"
    elif resistance > 10**3:
        resistance = str(resistance // 10**3) + " kiloohms"
    else:
        resistance = str(resistance) + " ohms"
    return resistance