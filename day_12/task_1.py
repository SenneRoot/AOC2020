from boat import Boat

def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]

def getInputDict():
    inputs = read_input("input.txt")

    instructions = dict()

    for i, input in enumerate(inputs):
        instructions[i] = (input[:1], input[1:])

    return instructions

if __name__ == "__main__":
    
    instructions = getInputDict()
    b = Boat({"R" : 1, "L" : -1})

    for instruction in instructions.values():
        b.performInstructionTask1(instruction[0], int(instruction[1]))

    print(b.manhattanDis())
