__color: dict = {
    "red":31,
    "green":32,
    "yellow":33,
    "blue":34,
    "cyan":36,
    "magenta":35,
}

def ColorPrint(a_str: str = '', a_color: str = None):
    color: int = None
    if a_color in __color:
        color = __color[a_color]
    else:
        color = 0
        
    print(f"\033[{color}m{a_str}\033[0m")