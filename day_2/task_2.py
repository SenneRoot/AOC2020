def read_input(filename):
     with open(filename) as f:
         return [str(x) for x in f]


def isValid(minCount, maxCount, letter, password):
    if (password[minCount - 1] != letter and password[maxCount - 1] != letter):
        return False
    elif(password[minCount - 1] == letter and password[maxCount - 1] == letter):
        return False
    elif (password[minCount - 1] == letter and password[maxCount - 1] != letter or password[minCount - 1] != letter and password[maxCount - 1] == letter):
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


            