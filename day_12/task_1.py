def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]

#boat = Boat()
turn = {"R" : 1,
        "L" : -1}

opposite = {"N" : "S",
            "E" : "W",
            "S" : "N",
            "W" : "E"}

boatState = {"N" : 0,
             "E" : 0,
             "S" : 0,
             "W" : 0,
             "F" : "E"}

direction = list(["N", "E", "S", "W"])

class Boat:
    def __init__(self, state):
        self.state = state

    def performInstruction(self, instruction, value):
        # turn
        if instruction == "L" or instruction == "R":
            boatState["F"] = direction[(direction.index(boatState["F"]) + int((turn[instruction] * (value/90)))) % len(direction)]
        elif instruction == "F":
            # add the value to the opposite direction were facing if this diection 
            if value < self.state[opposite[self.state[instruction]]]:
                self.state[opposite[self.state[instruction]]] -= value
            else:
                self.state[self.state[instruction]] += value - self.state[opposite[self.state[instruction]]]
                self.state[opposite[self.state[instruction]]] = 0
        else:
            if value < self.state[opposite[instruction]]:
                self.state[opposite[instruction]] -= value
            else:
                self.state[instruction] += (value - self.state[opposite[instruction]])
                self.state[opposite[instruction]] = 0
        


if __name__ == "__main__":
    inputs = read_input("input.txt")

    instructions = dict()

    for i, input in enumerate(inputs):
        instructions[i] = (input[:1], input[1:])

    b = Boat(boatState.copy())

    for instruction in instructions.values():
        b.performInstruction(instruction[0], int(instruction[1]))

    print(abs(b.state["N"] - b.state["S"]) + abs(b.state["E"] - b.state["W"]))
