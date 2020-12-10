def read_input(filename):
    return [int(x) for x in open(filename)]

def checkSums(inputs, number):
    for index, i in enumerate(inputs):
        index += 1
        for j in inputs[index:]:
            if i + j == number:
                return True
    return False

if __name__ == "__main__":
    inputs = read_input("input.txt")
    for index, i in enumerate(inputs):
        test = inputs[index:index+25]
        if not checkSums(test, inputs[(index + 25)]):
            print(inputs[index + 25])
            break
