
def read_input(filename):
    a = []
    with open(filename) as f:
        for line in f:
            a.append([c != "." for c in line.strip("\n")])
    return a            

def countTrees(rightSteps, downSteps, inputs):
    i = 0
    j = downSteps
    count = 0
    while j < len(inputs):
        i = (i + rightSteps) % len(inputs[0])
        count += inputs[j][i]
        j += downSteps
        
    return count 
        
inputs = read_input("input.txt")

numTrees = countTrees(3, 1, inputs)

print(numTrees)
    