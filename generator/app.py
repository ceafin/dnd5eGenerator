#
#
from generator.tables import generic, npcs, adventures
from generator.builders import tavern, npc, town
from generator.common import rollers


def run():
    place = generic.place()
    print(f"Rolled place: {place}")

    my_tavern = tavern.builder()
    print(f"Tavern Builder: {my_tavern}")

    characterStats = rollers.abilRollSet()
    print(characterStats)

    myNPC = npc.builder()
    print(myNPC)

    randomTown = town.builder()
    print(randomTown)

    print("Dungeon prompt: " + adventures.dungeonGoals())
    print("Wilderness prompt: " + adventures.wildernessGoals())
    print("Other prompt: " + adventures.otherGoals())


if __name__ == "__main__":
    print("Usage is: python -m generator")
