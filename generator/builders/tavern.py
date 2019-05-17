from random import choice, choices, randint
from generator.tables import taverns


def name():
    result = ""

    groups = {
        1: taverns.adj() + " " + taverns.creature(),
        2: taverns.adj() + " " + taverns.creature(),
        3: taverns.adj2() + " " + taverns.creature(),
        4: taverns.adj() + " " + taverns.item(),
        5: taverns.adj3() + " " + taverns.item(),
        6: taverns.adj() + " " + taverns.person(),
        7: taverns.adj2() + " " + taverns.person(),
        8: taverns.adj() + " " + taverns.place(),
        9: taverns.creature() + " and " + taverns.creature(),
        10: taverns.creature() + "'s " + taverns.item(),
        11: taverns.creature() + "'s " + taverns.item2(),
        12: taverns.creature() + "'s " + taverns.place(),
        13: taverns.item() + " and " + taverns.item(),
        14: taverns.person() + " and " + taverns.person(),
        15: taverns.person() + "'s " + taverns.item(),
        16: taverns.person() + "'s " + taverns.place(),
    }

    result = groups[randint(1, 16)]
    return result


def builder(count=1):
    
    if count > 1:
        results=[]
        for _ in range(count):
            result = "The " + name()
            if randint(1, 2) == 2:
                result = result + " " + taverns.bldg()
            results.append(result.title().replace("'S", "'s").replace("And", "and"))
        return results
    else:
        result = "The " + name()
        if randint(1, 2) == 2:
            result = result + " " + taverns.bldg()
        return result.title().replace("'S", "'s").replace("And", "and")
