import math

def getHalf(min, max, topHalf):
    middle = math.floor((min + max)  / 2)
    if topHalf:
        return min, middle
    else:
        return middle + 1, max

def decode_seat_number(seatString):
    minRow = 0
    maxRow = 127
    for char in seatString[0:7]:
        minRow, maxRow = getHalf(minRow, maxRow, char == "F")

    maxSeat = 7
    minSeat = 0
    for char in seatString[7:]:
        minSeat, maxSeat = getHalf(minSeat, maxSeat, char == "L")

    return 8 * maxRow + maxSeat

def read_input(filename):
     with open(filename) as f:
         return [str(x) for x in f]

inputs = read_input("input.txt")

print(max(decode_seat_number(input.strip("\n")) for input in inputs))


