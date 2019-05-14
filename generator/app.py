#
#
from generator.tables import generic
from generator.builders import tavern


def run():
    place = generic.place()
    print(f"Rolled place: {place}")

    my_tavern = tavern.builder()
    print(f"Tavern Builder: {my_tavern}")


if __name__ == "__main__":
    print("Usage is: python -m generator")
