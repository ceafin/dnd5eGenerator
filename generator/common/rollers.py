import random


def rollSuper():
    stat = []
    attrib = 0

    for i in range(6):
        roll = random.randint(1, 6)
        while roll == 1:
            roll = random.randint(1, 6)

        stat.append(roll)

    stat.remove(min(stat))
    stat.remove(min(stat))
    stat.remove(min(stat))

    for i in stat:
        attrib += i

    return attrib


def rollHeroic():
    stat = []
    attrib = 0

    for i in range(4):
        roll = random.randint(1, 6)
        while roll == 1:
            roll = random.randint(1, 6)

        stat.append(roll)

    stat.remove(min(stat))

    for i in stat:
        attrib += i

    return attrib


def rollClassic():
    attrib = 0

    for _ in range(3):
        roll = random.randint(1, 6)
        while roll == 1:
            roll = random.randint(1, 6)

        attrib += roll

    return attrib


def rollNPC():
    attrib = 0

    for i in range(3):
        i *= 1
        attrib += random.randint(1, 6)

    return attrib


def abilRollSet(k="CLASSIC"):
    abilSet = []

    for _ in range(6):
        if k == "SUPER":
            result = rollSuper()
        elif k == "HEROIC":
            result = rollHeroic()
        elif k == "CLASSIC":
            result = rollClassic()
        elif k == "NPC":
            result = rollNPC()
        else:
            result = 0

        abilSet.append(result)

    return abilSet
