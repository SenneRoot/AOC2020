from boat import Boat
from task_1 import read_input, getInputDict

if __name__ == "__main__":
    instructions = getInputDict()
    b = Boat({"R" : -1, "L" : 1})

    for instruction in instructions.values():
        b.performInstructionTask2(instruction[0], int(instruction[1]))

    print(b.manhattanDis())
