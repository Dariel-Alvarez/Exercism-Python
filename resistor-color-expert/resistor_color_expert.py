COLORS = ["black", "brown", "red", "orange", "yellow", 
          "green", "blue", "violet", "grey", "white"]

TOLERANCES = {"grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5,
              "brown": 1, "red": 2, "gold": 5, "silver": 10}

def resistor_label(colors):

    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

    if len(colors) == 4:
        color1, color2, multiplier, tolerance = colors
        resistance = int(f"{COLORS.index(color1)}{COLORS.index(color2)}") * (10 ** COLORS.index(multiplier))
    if len(colors) == 5:
        color1, color2, color3, multiplier, tolerance = colors
        resistance = int(f"{COLORS.index(color1)}{COLORS.index(color2)}{COLORS.index(color3)}") * (10 ** COLORS.index(multiplier))

    if resistance >= 10**9:
        resistance_str = f"{resistance / 10**9:g} gigaohms"
    elif resistance >= 10**6:
        resistance_str = f"{resistance / 10**6:g} megaohms"
    elif resistance >= 10**3:
        resistance_str = f"{resistance / 10**3:g} kiloohms"
    else:
        resistance_str = f"{resistance} ohms"

    return f"{resistance_str} ±{TOLERANCES[tolerance]}%"