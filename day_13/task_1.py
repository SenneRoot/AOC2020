import math

def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]

if __name__ == "__main__":

    inputs = read_input("input.txt")
    
    target = int(inputs.pop(0))
    times = [int(t) for t in inputs[0].split(",") if t !=  "x"]

    closeDict = dict()
    for time in times:
        closeDict[time] = time * math.ceil(target / time)


    closest = math.inf
    closestKey = 0
    for key, time in closeDict.items():
        if time < target:
            continue
        elif time - target < closest:
            closest = time - target
            closestKey = key
            
    
    print(closest * closestKey)