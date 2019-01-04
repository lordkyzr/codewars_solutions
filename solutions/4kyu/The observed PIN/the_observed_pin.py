from itertools import product


def get_pins(observed):
    combos = {
        "1": ["1", "2", "4"],
        "2": ["1", "2", "3", "5"],
        "3": ["2", "3", "6"],
        "4": ["1", "4", "5", "7"],
        "5": ["2", "5", "4", "6", "8"],
        "6": ["3", "6", "5", "9"],
        "7": ["4", "7", "8"],
        "8": ["5", "8", "7", "9", "0"],
        "9": ["6", "9", "8"],
        "0": ["8", "0"]
    }
    returnlst = []
    for item in observed:
        returnlst.append(combos[item])

    # Return an empty list if passed in values are empty
    if len(observed) == 0:
        return []

    # If there is only one item return possible values
    if len(observed) == 1:
        return returnlst[0]

    # We need to cartesian join and filter out dupes
    possible_combos = list(set(sorted(product(*returnlst))))
    return ["".join(item) for item in possible_combos]
