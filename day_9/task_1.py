def read_input(filename):
    return [int(x) for x in open(filename)]


def checkSums(inputs, number):
    i = 0 
    while i < len(inputs):
        j = i + 1 
        while j < len(inputs):
            if j != i and (inputs[i] + inputs[j]) == number:
                return True
            j += 1
        i += 1
    return False

if __name__ == "__main__":
    inputs = read_input("input.txt")
    
    i = 0
    while i < len(inputs):
        test = inputs[i:i+25]
        if not checkSums(test, inputs[i + 25]):
            print(inputs[i + 25])
            break
        else:
            i += 1
            pass