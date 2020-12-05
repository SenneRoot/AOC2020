def getHalf(min, max, topHalf):
    middle = int((min + max)  / 2)
    return (min, middle) if topHalf else (middle + 1, max)

def decode_seat_number(seatString, rowCount = 127, columnCount = 7):
    minRow, maxRow = 0, rowCount
    for char in seatString[0:7]:
        minRow, maxRow = getHalf(minRow, maxRow, char == "F")

    minSeat, maxSeat = 0, columnCount 
    for char in seatString[7:]:
        minSeat, maxSeat = getHalf(minSeat, maxSeat, char == "L")

    return 8 * maxRow + maxSeat

def read_input(filename):
    return [str(x) for x in open(filename)]

if __name__ == "__main__":
    print(max(decode_seat_number(input.strip("\n")) for input in read_input("input.txt")))
