from random import choice, choices, randint
from generator.tables import towns
import textwrap


def builder():
    result = "[Town Name], [size type], [population]: "

    result += "The relations here are " + towns.raceRelations() + ". "
    result += "Ruling status is " + towns.rulerStatus() + ". "
    result += "Notable trait(s) of: " + towns.notableTraits() + ". "
    result += "The town is known for " + towns.knownFor() + ". "
    result += "They are currently going through " + towns.currentCalamity() + ". "
    result = textwrap.fill(result, 72)

    return result
