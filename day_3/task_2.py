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

    print("Trees found: " + str(count) + " with stepsize: Right: " + str(rightSteps) + " Left: " + str(downSteps))
    return count
      
        
inputs = read_input("input.txt")
paths = [[1,1],[3,1],[5,1],[7,1],[1,2]]

answer = 1
for path in paths:
    answer *= countTrees(path[0], path[1], inputs)

print(answer)
