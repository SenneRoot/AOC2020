from task_1 import read_input, performInstruction

def test(instructions):
    instructionPointer = 0
    accumelator = 0
    runnedInstructions = {}
    while instructionPointer < len(instructions):
        instruction, arg = instructions[instructionPointer].split(" ")
        arg = int(arg)
        if instructionPointer in runnedInstructions.keys():
            return False, accumelator
        else:
            runnedInstructions[instructionPointer] = instruction

        accumelator, instructionPointer = performInstruction(instruction, arg, instructionPointer, accumelator)

    return True, accumelator

def force(instructions, ins, replace):
    # brute force that stuff
    for pos, val in ins.items():
        tmpIns = instructions.copy()
        tmpIns[pos] = replace + " " + tmpIns[pos].split(" ")[1]

        print(f"Switching line: {pos + 1} {val} to {tmpIns[pos]}")
        succes, result = test(tmpIns)
        if succes:
            print(f"Found a correct solve at line: {pos+1}, Acummelator value: {result}") 
            return True

    print("No solution found!")
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

    if force(instructions, jmps, "nop"):
        print("found a correct solve in jmp! See output above")
    elif force(instructions, nops, "jmp"):
        print("found correct solve in nop! See output above")

         


    