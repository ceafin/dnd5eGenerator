from random import choice, choices, randint


def place(count=1):
    elements = [
        "battlement",
        "bridge",
        "castle",
        "cave",
        "cove",
        "crag",
        "crypt",
        "den",
        "domain",
        "dungeon",
        "gate",
        "hall",
        "haven",
        "hideout",
        "hill",
        "house",
        "inn",
        "keep",
        "labyrinth",
        "lair",
        "landing",
        "manor",
        "nest",
        "oasis",
        "pit",
        "rest",
        "river",
        "road",
        "rookery",
        "roost",
        "sanctum",
        "shrine",
        "star",
        "temple",
        "throne",
        "tomb",
        "tower",
        "valley",
        "vault",
        "wood",
    ]
    if count > 1:
        return choices(elements, k=count)
    else:
        return choice(elements)
