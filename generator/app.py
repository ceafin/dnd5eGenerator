#
#
from generator.tables import generics


def run():
    place = generics.place()
    print(f"Rolled place: {place}")


if __name__ == "__main__":
    print("Usage is: python -m generator")
