def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]

inputs = read_integers("input.txt")

for i, input in enumerate(inputs): 
    for j, next in enumerate(inputs[i:]):
        sum = input + next
        if (sum == 2020):
            print("1: " + str(input) + " 2: " + str(next) + " sum: " + str(sum))
            print(input * next)
