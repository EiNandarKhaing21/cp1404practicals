COLOUR_TO_CODE = {"AQUA": "#00FFFF", "BANANA YELLOW": "#FFE135","BABY BLUE": "#89CFF0", "BABY PINK": "#F4C2C2",
                "BEAVER": "#9F8170", "BURGUNDY": "#800020", "CAMEL": "#C19A6B", "ASH GREY": "#B2BEB5", "AMBER": "FFBF00", "BONE": "E3DAC9"}

colour_code = input("Enter a colour: ").upper()
while colour_code != "":
    if colour_code in COLOUR_TO_CODE:
        print(f"{colour_code} is {COLOUR_TO_CODE[colour_code]}")
    else:
        print("Invalid colour!")
    colour_code = input("Enter a colour: ").upper()