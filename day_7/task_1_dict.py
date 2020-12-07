import re

def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]

def createBags(inputs):
    # regex to find all sub bags colors + count
    regex = re.compile(r"((\d+?) (.+?) bag)+")

    bagsDict = {}
    for line in inputs:
        outside, inside = line.split(" bags contain ")
        bags = regex.findall(inside)
        inside = {}

        for bag in bags:
            inside[bag[2]] = int(bag[1])

        # finally add the inner dict to the outer dict
        bagsDict[outside] = inside
    
    return bagsDict


def findBags(bagsToFind, bagsDict):
    foundBags = set()

    # continue while there are still bags to check
    while len(bagsToFind):
        findBag = bagsToFind.pop()
        bags = [bag for bag, innerBags in bagsDict.items() if findBag in innerBags]
        #update bags to find if a new sub bag is found:        
        bagsToFind.update(bags)
        #update the found bags, uses set to eliminate double values
        foundBags.update(bags)

    return foundBags


if __name__ == "__main__":
    bagsDict = createBags(read_input("input.txt"))
    foundBags = findBags({"shiny gold"}, bagsDict)

    print(len(foundBags))
