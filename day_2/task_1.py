def read_input(filename):
     with open(filename) as f:
         return [str(x) for x in f]


def isValid(minCount, maxCount, letter, password):
    letterCount = 0
    for i, index in enumerate(password):   
        if index == letter:
            letterCount += 1
        if letterCount > maxCount:
            return False

    if(letterCount < minCount):
        return False

    return True       


inputs = read_input("input.txt")


valid = 0
for i, input in enumerate(inputs):
    splitted = input.split()

    bounds = splitted[0].split("-")
    minCount = int(bounds[0])
    maxCount = int(bounds[1])

    letter = splitted[1].split(":")[0]

    password = splitted[2]

    if isValid(minCount, maxCount, letter, password):
        valid += 1

print(valid)


            