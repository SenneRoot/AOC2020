import re

def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]

class Bag:
    def __init__(self, color):
        self.color = color
        self.innerBags = {}

    def addInnerBag(self, innerBagColor, count):
        self.innerBags[innerBagColor] = count


def createBags(inputs):
    # regex to find all sub bags colors + count
    regex = re.compile(r"((\d+?) (.+?) bag)+")

    bagsList = []
    for line in inputs:
        outside, inside = line.split(" bags contain ")
        bags = regex.findall(inside)
        b = Bag(outside)

        for bag in bags:
            b.addInnerBag(bag[2], int(bag[1]) )

        # finally add the inner dict to the bag
        bagsList.append(b) 
    
    return bagsList


def findBags(bagsToFind, bagList):
    foundBags = set()

    # continue while there are still bags to check
    while len(bagsToFind):
        findBag = bagsToFind.pop()
        bags = [bag.color for bag in bagsList if findBag in bag.innerBags]
        #update bags to find if a new sub bag is found:        
        bagsToFind.update(bags)
        #update the found bags, uses set to eliminate double values
        foundBags.update(bags)

    return foundBags


if __name__ == "__main__":
    bagsList = createBags(read_input("input.txt"))
    foundBags = findBags({"shiny gold"}, bagsList)

    print(len(foundBags))
