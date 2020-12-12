class Boat:
    def __init__(self, turn):
        # Startin state, only keep track of N. E:  -N is S and -E is W
        self.state = {"N" : 0, "E" : 0, "F" : "E"}
        # need to translate instructions S -> N and W -> E
        self.instructions = {"N" : "N", "E" : "E", "S" : "N", "W" : "E"}
        # N and E are + and S and W are -
        self.move = {"N" : 1, "E" : 1, "S" : -1, "W" : -1}
        # turn for task one and two are inverted so ask for correct dict
        self.turn = turn
        # this list is used for rotating
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
            for key in self.wayPoint.keys():
                # move to the waypoint * value * direction(- or +)
                self.state[self.instructions[key]] += self.wayPoint[key] * value * self.move[key]
        else:
            self.moveWaypoint(instruction, value)

    def moveWaypoint(self, instruction, value):
        # rotate r: e = n, s = e, w = s, n = w
        # rotate l: e = s, s = w, w = n, n = e
        if instruction == "L" or instruction == "R":
            newWaypoint = self.wayPoint.copy()
            for key in self.wayPoint.keys():
                newWaypoint[key] = self.wayPoint[self.direction[((self.direction.index(key) + int(self.turn[instruction] * (value/90)))) % len(self.direction)]]
                # assign rotated waypoint
            self.wayPoint = newWaypoint
        else: #instruction = N, E, S, W
            self.wayPoint[self.instructions[instruction]] += value * self.move[instruction]


    def manhattanDis(self):
        return abs(self.state["N"]) + abs(self.state["E"])
