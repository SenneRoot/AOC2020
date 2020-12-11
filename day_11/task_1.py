import copy

def read_input(filename):
    return [list(line.rstrip()) for line in open(filename)]

stateDict = {'.' : 0,#floor
             'L' : 1,#empty
             '#' : 2}#occupied

def countOccupied(inputs):
    count = 0
    for row in inputs:
        for seat in row:
            if stateDict[seat] == 2:
                count += 1
    return count

# returns True if there is a adjecent seat, false if not
def checkAdjecentSeats(inputs, rowIndex, seatIndex):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for y, x in directions:
        dY, dX =  rowIndex + y, seatIndex + x
        if dY >= 0 and dY < len(inputs) and dX >= 0 and dX < len(inputs[0]):
            if stateDict[inputs[dY][dX]] == 2:
                count += 1
                
    return count

def gameOfSeats(inputs):
    newlayout = copy.deepcopy(inputs)

    for rowIndex, row in enumerate(inputs):
        for seatIndex, seat in enumerate(row):
            # rule one, If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if stateDict[seat] == 1 and not checkAdjecentSeats(inputs, rowIndex, seatIndex):
                newlayout[rowIndex][seatIndex] = '#'
            # rule two, If a seat is occupied (#) and MAX_OCCUPIED or more seats adjacent to it are also occupied, the seat becomes empty.    
            elif stateDict[seat] == 2 and checkAdjecentSeats(inputs, rowIndex, seatIndex) >= 4:
                newlayout[rowIndex][seatIndex] = 'L'
            
        
    return newlayout


if __name__ == "__main__":
    res = read_input("input.txt")

    prevRes = []
    while res != prevRes:
        prevRes = res
        res = gameOfSeats(res)

    print(countOccupied(res))

    