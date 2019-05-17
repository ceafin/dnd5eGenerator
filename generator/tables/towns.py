from random import choice, choices, randint


def randPop(label=""):

    size = {
        "Thorp": randint(20, 80),
        "Hamlet": randint(80, 400),
        "Village": randint(400, 900),
        "Small Town": randint(900, 2000),
        "Large Town": randint(2000, 5000),
        "Small City": randint(5000, 12000),
        "Large City": randint(12000, 25000),
        "Metropolis": randint(25001, 29999),
    }

    if not label:
        return size[randSize()]
    else:
        return size[label()]


def randSize():
    community = [
        "Thorp",
        "Hamlet",
        "Village",
        "Small Town",
        "Large Town",
        "Small City",
        "Large City",
        "Metropolis",
    ]
    return choices(community, [1, 5, 10, 20, 20, 10, 5, 1], k=1)[0]


def raceRelations():
    elements = [
        "Harmony",
        "Tension or rivalry",
        "Racial majority are conquerors",
        "Racial minority are rulers",
        "Racial minority are refugees",
        "Racial majority oppresses minority",
        "Racial minority oppresses majority",
    ]
    return choices(elements, weights=[10, 4, 2, 1, 1, 1, 1])[0]


def rulerStatus():
    elements = [
        "Respected, fair, and just",
        "Feared tyrant",
        "Weakling manipulated by others",
        "Illegitimate ruler, simmering civil war",
        "Ruled or controlled by a powerful monster",
        "Mysterious, anonymous cabal",
        "Contested leadership, open fighting",
        "Cabal seized power openly",
        "Doltish lout",
        "On deathbed, claimants compete for power",
        "Iron-willed but respected",
        "Religious leader",
    ]
    return choices(elements, weights=[5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2])[0]


def notableTraits():
    elements = [
        "Canals in place of streets",
        "Massive statue or monument",
        "Grand temple",
        "Large fortress",
        "Verdant parks and orchards",
        "River divides town",
        "Major trade center",
        "Headquarters ofa powerful family or guild",
        "Population mostly wealthy",
        "Destitute, rundown",
        "Awful smell (tanneries, open sewers)",
        "Center of trade for one specific good",
        "Site of many battles",
        "Site of a mythic or magical event",
        "Important library or archive",
        "Worship of all gods banned",
        "Sinister reputation",
        "Notable library or academy",
        "Site of important tomb or graveyard",
        "Built atop ancient ruins",
    ]
    return choice(elements)


def knownFor():
    elements = [
        "Delicious cuisine",
        "Rude people",
        "Greedy merchants",
        "Artists and writers",
        "Great hero/savior",
        "Flowers",
        "Hordes of beggars",
        "Tough warriors",
        "Dark magic",
        "Decadence",
        "Piety",
        "Gambling",
        "Godlessness",
        "Education",
        "Wines",
        "High fashion",
        "Political intrigue",
        "Powerful guilds",
        "Strong drink",
        "Patriotism",
    ]
    return choice(elements)


def currentCalamity():
    elements = [
        "Suspected vampire infestation",
        "New cult seeks converts",
        "Important figure died (murder suspected)",
        "War between rival thieves' guilds",
        "Plague or famine (sparks riots)",
        "Corrupt officials",
        "Marauding monsters",
        "Powerful wizard has moved into town",
        "Economic depression (trade disrupted)",
        "Flooding",
        "Undead stirring in cemeteries",
        "Prophecy ofdoom",
        "Brink ofwar",
        "Internal strife (leads to anarchy)",
        "Besieged by enemies",
        "Scandal threatens powerful families",
        "Dungeon discovered (adventurers flock to town)",
        "Religious sects struggle for power",
    ]
    return choices(elements, weights=[1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])[0]


def spawnBuilding():
    def _Residence():
        elements = [
            "Abandoned squat",
            "Middle-class home",
            "Upper-class home",
            "Crowded tenement",
            "Orphanage",
            "Hidden slavers' den",
            "Front for a secret cult",
            "Lavish, guarded mansion",
        ]
        return choices(elements, weights=[2, 6, 2, 5, 2, 1, 1, 1])[0]

    def _Religious():
        elements = [
            "Temple to a good or neutral deity",
            "Temple to afalse deity (run bycharlatan priests)",
            "Home of ascetics",
            "Abandoned shrine",
            "Library dedicated to religious study",
            "Hidden shrine to a fiend or an evil deity",
        ]
        return choices(elements, weights=[10, 2, 1, 2, 2, 3])[0]

    def _Tavern():
        import generator.builders.tavern

        return generator.builders.tavern.builder()

    def _Warehouse():
        elements = [
            "Empty or abandoned",
            "Heavily guarded, expensive goods",
            "Cheap goods",
            "Bulk goods",
            "Live animals",
            "Weaponsfarmor",
            "Goods from a distant land",
            "Secret smuggler's den",
        ]
        return choices(elements, weights=[4, 2, 3, 4, 1, 2, 2, 1])[0]

    def _Shop():
        elements = [
            "Pawnshop",
            "Herbs/incense",
            "Fruitsfvegetables",
            "Dried meats",
            "Pottery",
            "Undertaker",
            "Books",
            "Moneylender",
            "Weaponsfarmor",
            "Chandler",
            "Smithy",
            "Carpenter",
            "Weaver",
            "Jeweler",
            "Baker",
            "Mapmaker",
            "Tailor",
            "Ropemaker",
            "Mason",
            "Scribe",
        ]
        return choice(elements)

    buildingType = {
        "A": _Residence(),
        "B": _Religious(),
        "C": _Tavern(),
        "D": _Warehouse(),
        "E": _Shop(),
    }
    elements = ["A", "B", "C", "D", "E"]
    building = choices(elements, weights=[10, 2, 3, 2, 3])[0]
    return buildingType[building]
