from task_1 import stateDict, countOccupied, read_input
import copy

# returns True if there is a adjecent seat, false if not
def checkAdjecentSeats(inputs, rowIndex, seatIndex):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for y, x in directions:
        dY, dX =  rowIndex + y, seatIndex + x
        while (dY >= 0 and dY < len(inputs) and dX >= 0 and dX < len(inputs[0])):
            if stateDict[inputs[dY][dX]] != 0:
                count = count + 1 if inputs[dY][dX] == '#' else count
                break
            dY += y
            dX += x

    return count

def gameOfSeats(inputs):
    newlayout = copy.deepcopy(inputs)

    for rowIndex, row in enumerate(inputs):
        for seatIndex, seat in enumerate(row):
            # rule one, If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if stateDict[seat] == 1 and not checkAdjecentSeats(inputs, rowIndex, seatIndex):
                newlayout[rowIndex][seatIndex] = '#'
            # rule two, If a seat is occupied (#) and MAX_OCCUPIED or more seats adjacent to it are also occupied, the seat becomes empty.    
            elif stateDict[seat] == 2 and checkAdjecentSeats(inputs, rowIndex, seatIndex) >= 5:
                newlayout[rowIndex][seatIndex] = 'L'
            
        
    return newlayout

if __name__ == "__main__":
    res = read_input("input.txt")

    prevRes = []
    while res != prevRes:
        prevRes = res
        res = gameOfSeats(res)

    print(countOccupied(res))