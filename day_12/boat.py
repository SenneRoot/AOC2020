class Boat:
    def __init__(self, turn):
        # only keep track of N. E:  -N is S and -E is W
        self.state = {"N" : 0, "E" : 0, "F" : "E"}
        # need to translate S -> N and W -> E
        self.instructions = {"N" : "N", "E" : "E", "S" : "N", "W" : "E"}
        # N and E are + and S and W are -
        self.move = {"N" : 1, "E" : 1, "S" : -1, "W" : -1}
        # turn for task one and two are inverted so ask for correct dict
        self.turn = turn
        # this lsit is used for rotating
        self.direction = list(["N", "E", "S", "W"])
        self.wayPoint = {"N" : 1, "E" : 10, "S" : 0, "W" : 0}

    def performInstructionTask1(self, instruction, value):
        # turn
        if instruction == "L" or instruction == "R":
            self.state["F"] = self.direction[(self.direction.index(self.state["F"]) + int((self.turn[instruction] * (value/90)))) % len(self.direction)]
        elif instruction == "F":
            # add the value to the opposite direction were facing if this diection
            self.state[self.instructions[self.state[instruction]]] += value * self.move[self.state[instruction]]
        else:
            self.state[self.instructions[instruction]] += value * self.move[instruction]
    
    def performInstructionTask2(self, instruction, value):
        if instruction == "F":
            #perform step value times
            for key in self.wayPoint.keys():
                step = self.wayPoint[key] * value
                self.state[self.instructions[key]] += step * self.move[key]
        else:
            self.moveWaypoint(instruction, value)

    def moveWaypoint(self, instruction, value):
        # rotate: e += n, s += e, , w += s, n += w
        if instruction == "L" or instruction == "R":
            newWaypoint = self.wayPoint.copy()
            for i in range(0, int(value/90)):
                for key in self.wayPoint.keys():
                    newWaypoint[key] = self.wayPoint[self.direction[(self.direction.index(key) + self.turn[instruction]) % len(self.direction)]]
                self.wayPoint = newWaypoint.copy()
        else: #instruction = N, E, S, W
                self.wayPoint[self.instructions[instruction]] += value * self.move[instruction]


    def manhattanDis(self):
        return abs(self.state["N"]) + abs(self.state["E"])
