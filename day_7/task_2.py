from task_1 import read_input, createBags

def countBagsInside(bagsToFind, bagList):
    counter = 0
    # this time we dont use a set, because we need to count all occurences
    while len(bagsToFind):
        # get bag and remove from list
        bag = bagsToFind.pop()

        for b in bagList:
            if b.color == bag:
                inside = b.innerBags
                break
        # process the sub bags
        for color, count in inside.items():
            counter += count
            bagsToFind.extend([color] * count)

    return counter

if __name__ == "__main__":
    bagList = createBags(read_input("input.txt"))
    count = countBagsInside(["shiny gold"], bagList)

    print(count)