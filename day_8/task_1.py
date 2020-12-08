def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]

def performInstruction(instruction, arg, instructionPointer, accumelator):
    if instruction == "nop":
        instructionPointer += 1
        return accumelator, instructionPointer
    elif instruction == "acc":
        instructionPointer += 1
        accumelator += arg
        return accumelator, instructionPointer
    elif instruction == "jmp":
        instructionPointer += arg
        return accumelator, instructionPointer

if __name__ == "__main__":
    instructions = read_input("input.txt")

    runnedInstructions = {}
    accumelator = 0
    instructionPointer = 0
    while instructionPointer < len(instructions):
        instruction, arg = instructions[instructionPointer].split(" ")
        arg = int(arg)
        if instructionPointer in runnedInstructions.keys():
            print("We are looping at: " + instructions[instructionPointer])
            break
        else:
            runnedInstructions[instructionPointer] = instructions[instructionPointer]

        accumelator, instructionPointer = performInstruction(instruction, arg, instructionPointer, accumelator)

    
    print(accumelator)

    