import math

def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]

if __name__ == "__main__":

    inputs = read_input("input.txt")
    
    target = int(inputs.pop(0))
    times = [int(t) for t in inputs[0].split(",") if t !=  "x"]

    closeDict = dict()
    for time in times:
        closeDict[time] = [time * (target // time), time * math.ceil(target / time)]


    closest = 10000000000
    closestKey = 0
    for key, times in closeDict.items():
        for time in times:
            if time < target:
                continue
            elif time - target < closest:
                closest = time - target
                closestKey = key
            
    
    print(closest * closestKey)