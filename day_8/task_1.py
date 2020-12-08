def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]

def performInstruction(instruction, arg, instructionPointer, accumelator):
    if instruction == "nop":
        return accumelator, instructionPointer + 1
    elif instruction == "acc":
        return accumelator + arg, instructionPointer + 1
    elif instruction == "jmp":
        return accumelator, instructionPointer + arg
    else:
        print("Unsupported instruction!")


def findLoop(instructions):
    runnedInstructions = dict()
    accumelator = 0
    instructionPointer = 0
    while instructionPointer < len(instructions):
        instruction, arg = instructions[instructionPointer].split(" ")
        arg = int(arg)
        if instructionPointer in runnedInstructions.keys():
            return False, accumelator, instructionPointer
        else:
            runnedInstructions[instructionPointer] = instructions[instructionPointer]

        accumelator, instructionPointer = performInstruction(instruction, arg, instructionPointer, accumelator)

    return True, accumelator, instructionPointer


if __name__ == "__main__":
    result, accumelator, instructionPointer = findLoop(read_input("input.txt"))
    print(f"Found loop at: {instructionPointer} With accumulator value  of: {accumelator}")