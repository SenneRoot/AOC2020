import math

def getHalf(min, max, topHalf):
    middle = math.floor((min + max)  / 2)
    if topHalf:
        return min, middle
    else:
        return middle + 1, max

def decode_seat_number(seatString):
    rowString = seatString[0:7]
    colString = seatString[7:]

    minRow = 0
    maxRow = 127
    for char in rowString:
        minRow, maxRow = getHalf(minRow, maxRow, char == "F")

    maxSeat = 7
    minSeat = 0
    for char in colString:
        minSeat, maxSeat = getHalf(minSeat, maxSeat, char == "L")

    row = maxRow
    seat = maxSeat

    return 8 * row + seat

def read_input(filename):
     with open(filename) as f:
         return [str(x) for x in f]

inputs = read_input("input.txt")

maxSeatID = 0
for input in inputs:
    seatID = decode_seat_number(input.strip("\n"))
    if seatID > maxSeatID:
        maxSeatID = seatID

print(maxSeatID)

