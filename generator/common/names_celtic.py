from random import choice, choices, randint


def prefM():
    elements = [
        "Ad",
        "Addr",
        "Aeth",
        "Air",
        "Al",
        "An",
        "Ans",
        "Ar",
        "Bed",
        "Bl",
        "Bow",
        "C",
        "Cad",
        "Cal",
        "Car",
        "Ced",
        "Con",
        "Cor",
        "Cul",
        "D",
        "Dar",
        "Der",
        "Dev",
        "Don",
        "Dr",
        "Dunh",
        "Er",
        "Ev",
        "Ew",
        "Ferg",
        "Fin",
        "G",
        "Gl",
        "Gw",
        "Hal",
        "Inn",
        "K",
        "Kel",
        "Ken",
        "L",
        "M",
        "Mer",
        "Mor",
        "Nol",
        "Or",
        "Ow",
        "P",
        "Pw",
        "Qu",
        "R",
        "Rh",
        "S",
        "Sher",
        "Sl",
        "T",
        "Tr",
        "V",
        "Yr",
    ]
    return choice(elements)


def midM():
    elements = ["a", "ae", "e", "eo", "i", "o", "u", "y"]
    return choice(elements)


def suffM():
    elements = [
        "air",
        "al",
        "am",
        "an",
        "ant",
        "awn",
        "bad",
        "bryn",
        "c",
        "ce",
        "cyn",
        "dan",
        "dd",
        "ddry",
        "ddyn",
        "der",
        "doc",
        "don",
        "dric",
        "dry",
        "dyn",
        "ell",
        "en",
        "ey",
        "gan",
        "gar",
        "gda",
        "gh",
        "git",
        "gus",
        "gwyn",
        "gyle",
        "hern",
        "ine",
        "lan",
        "len",
        "lin",
        "llyn",
        "loch",
        "lyn",
        "mac",
        "man",
        "myr",
        "n",
        "nall",
        "nan",
        "ney",
        "nnyn",
        "nry",
        "nvan",
        "nyc",
        "r",
        "ran",
        "rcyn",
        "ric",
        "rol",
        "roy",
        "rraent",
        "rry",
        "rth",
        "ryn",
        "s",
        "son",
        "thur",
        "tur",
        "vin",
        "well",
        "wn",
        "wyl",
        "wyr",
    ]
    return choice(elements)


def prefF():
    elements = [
        "A",
        "Al",
        "Ar",
        "Arl",
        "Be",
        "Birg",
        "Br",
        "C",
        "Cl",
        "Cord",
        "D",
        "D",
        "Dag",
        "De",
        "Dor",
        "El",
        "Fi",
        "Gw",
        "Is",
        "J",
        "L",
        "M",
        "Mer",
        "Morr",
        "N",
        "R",
        "Row",
        "S",
        "Wyn",
        "Ys",
    ]
    return choice(elements)


def midF():
    elements = ["a", "ae", "e", "ea", "i", "o", "u", "y", "w"]
    return choice(elements)


def suffF():
    elements = [
        "cla",
        "da",
        "dra",
        "ena",
        "eve",
        "gan",
        "ghid",
        "git",
        "ld",
        "lia",
        "ll",
        "lla",
        "lona",
        "lyan",
        "lyra",
        "n",
        "na",
        "ne",
        "neve",
        "nn",
        "noic",
        "ra",
        "rdre",
        "ria",
        "ryan",
        "ryla",
        "ssa",
        "t",
        "tha",
        "vona",
        "vyan",
        "wen",
    ]
    return choice(elements)


def create(s="M"):
    groups = {0: prefM() + midM() + suffM() + " (m.)", 1: prefF() + midF() + suffF() + " (f.)"}

    if s == "M":
        result = groups[0]
    elif s == "F":
        result = groups[1]
    else:
        result = groups[randint(0, 1)]

    return result
