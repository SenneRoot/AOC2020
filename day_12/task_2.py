def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]

turn = {"R" : -1,
        "L" : 1}

opposite = {"N" : "S",
            "E" : "W",
            "S" : "N",
            "W" : "E"}

boatState = {"N" : 0,
             "E" : 0,
             "S" : 0,
             "W" : 0,
             "F" : "E"}

wayPoint = {"N" : 1,
            "E" : 10,
            "S" : 0,
            "W" : 0,}

direction = list(["N", "E", "S", "W"])


class Boat:
    def __init__(self, state, wayPoint):
        self.state = state.copy()
        self.wayPoint = wayPoint.copy()

    def performInstruction(self, instruction, value):
        if instruction == "F":
            #perform step value times
            for key in self.wayPoint.keys():
                step = self.wayPoint[key] * value
                # add the value to the opposite direction were facing if this diection 
                if step < self.state[opposite[key]]:
                    self.state[opposite[key]] -= step
                else:
                    self.state[key] += step - self.state[opposite[key]]
                    self.state[opposite[key]] = 0

           
    def moveWaypoint(self, instruction, value):
        # rotate: e += n, s += e, , w += s, n += w
        if instruction == "L" or instruction == "R":
            newWaypoint = self.wayPoint.copy()
            for i in range(0, int(value/90)):
                for key in self.wayPoint.keys():
                    newWaypoint[key] = self.wayPoint[direction[(direction.index(key) + turn[instruction]) % len(direction)]]
                self.wayPoint = newWaypoint.copy()
        else: #instruction = N, E, S, W
            if value < self.wayPoint[opposite[instruction]]:
                self.wayPoint[opposite[instruction]] -= value
            else:
                self.wayPoint[instruction] += (value - self.wayPoint[opposite[instruction]])
                self.wayPoint[opposite[instruction]] = 0
        

if __name__ == "__main__":
    inputs = read_input("input.txt")

    instructions = dict()

    for i, input in enumerate(inputs):
        instructions[i] = (input[:1], input[1:])

    b = Boat(boatState, wayPoint)

    for instruction in instructions.values():
        if instruction[0] != "F":
            b.moveWaypoint(instruction[0], int(instruction[1]))
        else:
            b.performInstruction(instruction[0], int(instruction[1]))

    print(abs(b.state["N"] - b.state["S"]) + abs(b.state["E"] - b.state["W"]))
