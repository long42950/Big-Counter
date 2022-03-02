from enum import Enum

front_margin = 0
mid_margin = 0
back_margin = 0

class Number(Enum):
    ONE = "  __ \n /_ |\n  | |\n  | |\n  | |\n  |_|\n     "
    TWO = "  ___  \n |__ \ \n    ) |\n   / / \n  / /_ \n |____|\n        "
    THREE = "  ____  \n |___ \ \n   __) |\n  |__ < \n  ___) |\n |____/ \n        "
    FOUR = "  _  _   \n | || |  \n | || |_ \n |__   _|\n    | |  \n    |_|  \n         "
    FIVE = "  _____ \n | ____|\n | |__  \n |___ \ \n  ___) |\n |____/ \n        "
    SIX = "    __  \n   / /  \n  / /_  \n | '_ \ \n | (_) |\n  \___/ \n        "
    SEVEN = "  ______ \n |____  |\n     / / \n    / /  \n   / /   \n  /_/    \n         "
    EIGHT = "   ___  \n  / _ \ \n | (_) |\n  > _ < \n | (_) |\n  \___/ \n        "
    NINE = "   ___  \n  / _ \ \n | (_) |\n  \__, |\n    / / \n   /_/  \n        "
    ZERO = "   ___  \n  / _ \ \n | | | |\n | | | |\n | |_| |\n  \___/ \n        "
    MINUS = "         \n         \n  ______ \n |______|\n         \n         \n         "

def show_number(num):
    global front_margin, mid_margin, back_margin
    txts = str(num)
    num_str = []
    rtn_value = ""
    for txt in txts:
        match txt:
            case '1':
                num_str.append(Number.ONE.value.split("\n"))
                continue
            case '2':
                num_str.append(Number.TWO.value.split("\n"))
                continue
            case '3':
                num_str.append(Number.THREE.value.split("\n"))
                continue
            case '4':
                num_str.append(Number.FOUR.value.split("\n"))
                continue
            case '5':
                num_str.append(Number.FIVE.value.split("\n"))
                continue
            case '6':
                num_str.append(Number.SIX.value.split("\n"))
                continue
            case '7':
                num_str.append(Number.SEVEN.value.split("\n"))
                continue
            case '8':
                num_str.append(Number.EIGHT.value.split("\n"))
                continue
            case '9':
                num_str.append(Number.NINE.value.split("\n"))
                continue
            case '0':
                num_str.append(Number.ZERO.value.split("\n"))
                continue
            case '-':
                num_str.append(Number.MINUS.value.split("\n"))
                continue
            case _:
                continue
    #rtn_value = " "*front_margin + "="*mid_margin + "="*back_margin + "="*len(num_str[0]) + "\n"
    for i in range(7):
        rtn_value += " "*front_margin
        for number in num_str:
            rtn_value += number[i]
            rtn_value += " "*mid_margin
        rtn_value += " "*back_margin
        rtn_value += "\n"
    return rtn_value

def set_front_margin(value):
    global front_margin
    if value >= 0:
        front_margin = value

def set_mid_margin(value):
    global mid_margin
    if value >= 0:
        mid_margin = value

def set_back_margin(value):
    global back_margin
    if value >= 0:
        back_margin = value
