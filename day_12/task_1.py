def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]

class Boat:
    def __init__(self):
        self.state = {"N" : 0, "E" : 0, "F" : "E"}
        self.instructions = {"N" : "N", "E" : "E", "S" : "N", "W" : "E"}
        self.move = {"N" : 1, "E" : 1, "S" : -1, "W" : -1}
        self.turn = {"R" : 1, "L" : -1}
        self.direction = list(["N", "E", "S", "W"])

    def performInstruction(self, instruction, value):
        # turn
        if instruction == "L" or instruction == "R":
            self.state["F"] = self.direction[(self.direction.index(self.state["F"]) + int((self.turn[instruction] * (value/90)))) % len(self.direction)]
        elif instruction == "F":
            # add the value to the opposite direction were facing if this diection
            self.state[self.instructions[self.state[instruction]]] += value * self.move[self.state[instruction]]
        else:
            self.state[self.instructions[instruction]] += value * self.move[instruction]
    
    def manhattanDis(self):
        return abs(self.state["N"]) + abs(self.state["E"])


if __name__ == "__main__":
    inputs = read_input("input.txt")

    instructions = dict()

    for i, input in enumerate(inputs):
        instructions[i] = (input[:1], input[1:])

    b = Boat()

    for instruction in instructions.values():
        b.performInstruction(instruction[0], int(instruction[1]))

    print(b.manhattanDis())
