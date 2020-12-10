def read_input(filename):
    return [int(x) for x in open(filename)]

if __name__ == "__main__":
    adapters = read_input("input.txt")
    joltDif = {1 : 0,
               3 : 0}

    # Append the final one (input for the device)
    adapters.append(max(adapters) + 3)
    adapters.sort()

    output = 0
    for adapter in adapters:
        joltDif[adapter - output] += 1
        output = adapter

    print(joltDif[1] * joltDif[3])
