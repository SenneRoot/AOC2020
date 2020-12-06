def read_input(filename):
    return [str(x) for x in open(filename)]


if __name__ == "__main__":
    inputs = read_input("input.txt")

    data = []
    count = 0
    for input in inputs:
        if input == "\n":
            count += len(set(data))
            data = []
        else:
            for char in input.strip("\n"):
                data.append(char)

    print(count)
