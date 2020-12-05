from task_1 import read_input, decode_seat_number

if __name__ == "__main__":
    inputs = read_input("input.txt")

    seatsIDs = [decode_seat_number(input.strip("\n")) for input in inputs]

    seatsIDs.sort()
    for i, seatid in enumerate(seatsIDs):
        if (i < len(seatsIDs) - 1):
            if seatsIDs[i + 1] == seatid + 2: 
                print(seatid + 1)

