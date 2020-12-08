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


def test(instructions):
    instructionPointer = 0
    accumelator = 0
    runnedInstructions = {}
    while instructionPointer < len(instructions):
        instruction, arg = instructions[instructionPointer].split(" ")
        arg = int(arg)
        if instructionPointer in runnedInstructions.keys():
            return False
        else:
            runnedInstructions[instructionPointer] = instruction

        accumelator, instructionPointer = performInstruction(instruction, arg, instructionPointer, accumelator)

    return True

def force(instructions, ins):
    # brute force that stuff
    for pos, val in ins.items():
        print("trying: " + str(pos + 1) + " " + str(val))

        tmpIns = instructions.copy()
        newIns = "nop +1"
        tmpIns[pos] = newIns

        if test(tmpIns):
            print("Found a correct solve at line: " + str(pos+1)) 
            return True
    return False


if __name__ == "__main__":
    instructions = read_input("input.txt")

    instructionPointer = 0
    total = 0

    jmps = {}
    nops = {}

    # get jmps and nops
    while instructionPointer < len(instructions):
        instruction, arg = instructions[instructionPointer].split(" ")
        arg = int(arg)

        if instruction == "jmp":
            jmps[instructionPointer] = instructions[instructionPointer]
        elif instruction == "nop":
            nops[instructionPointer] = instructions[instructionPointer]
             
        instructionPointer += 1

    if force(instructions, jmps):
        print("found correct solve in jmp! See output above")
    if force(instructions, nops):
        print("found correct solve in nop! See output above")

        


    