def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]

inputs = read_integers("input.txt")

for i, first in enumerate(inputs): 
    for j, second in enumerate(inputs[i:]):
        for k, third in enumerate(inputs[j:]):
            sum = first + second + third
            if (sum == 2020):
                print("1: " + str(first) + " 2: " + str(second) + " 3: " + str(third) + " sum: " + str(sum))
                print(first * second * third)
                exit()
