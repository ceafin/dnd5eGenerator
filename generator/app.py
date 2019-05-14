#
#
from generator.tables import generic
from generator.builders import tavern
from generator.common import rollers


def run():
    place = generic.place()
    print(f"Rolled place: {place}")

    my_tavern = tavern.builder()
    print(f"Tavern Builder: {my_tavern}")

    characterStats = rollers.abilRollSet()
    print(characterStats)


if __name__ == "__main__":
    print("Usage is: python -m generator")
