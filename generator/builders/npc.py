from random import choice, choices, randint
from generator.tables import npcs
import textwrap


def builder():

    result = ""
    sex = "she" if randint(1, 2) == 1 else "he"

    if sex == "he":
        npcName = npcs.name("M")
    elif sex == "she":
        npcName = npcs.name("F")
    else:
        npcName = npcs.name()

    result += npcName + " stands before you. "
    result += sex.capitalize() + " " + npcs.appearance() + ". "
    result += npcName + " " + npcs.abilities() + ". "
    result += sex.capitalize() + " " + npcs.talents() + ". "
    result += npcName + " " + npcs.mannerisms() + ". "
    result += "When interacting with others " + sex + " " + npcs.interactionTraits() + ". "
    result += npcName + " " + npcs.ideals() + ". "
    result += sex.capitalize() + " " + npcs.bonds() + ". "
    result += (
        "Something that could potentially undermine " + npcName + " " + npcs.flawsSecrets() + ".\n"
    )
    result = textwrap.fill(result, 72)

    return result
