from task_1_dict import read_input, createBags

def findBags(bagsToFind, bagsDict):
    counter = 0
    # this time we dont use a set, because we need to count all occurences
    while len(bagsToFind):
        # get bag and remove from list
        bag = bagsToFind.pop()
        inside = bagsDict[bag]
        # process the sub bags
        for color, count in inside.items():
            counter += count
            bagsToFind.extend([color] * count)

    return counter

if __name__ == "__main__":
    bagsDict = createBags(read_input("input.txt"))
    count = findBags(["shiny gold"], bagsDict)

    print(count)