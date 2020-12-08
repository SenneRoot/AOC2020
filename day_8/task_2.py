from task_1 import read_input, performInstruction, findLoop

def force(instructions, ins, replace):
    # brute force that stuff
    for pos, val in ins.items():
        tmpIns = instructions.copy()
        tmpIns[pos] = replace + " " + tmpIns[pos].split(" ")[1]

        print(f"Switching line {pos + 1}: \"{val}\" to \"{tmpIns[pos]}\"")
        succes, result, ins = findLoop(tmpIns)
        if succes:
            print(f"Found a correct solve at line {pos+1}: Acummelator value: {result}") 
            return True

    print("No solution found!")
    return False


if __name__ == "__main__":
    instructions = read_input("input.txt")

    instructionPointer = 0
    total = 0

    jmps = dict()
    nops = dict()

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

         


    