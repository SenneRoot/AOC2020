from task_1 import read_input
import math


def findFirstTime(inputs):
    data = [(i, int(id)) for i, id in enumerate(inputs[1].split(',')) if id != 'x']
    jump = data[0][1]
    time = 0
    for dT, id in data[1:]:
        while (time + dT) % id != 0:
            time += jump
        jump *= id
    return time


if __name__ == "__main__":

    inputs = read_input("input.txt")
    
    print(findFirstTime(inputs))

   

