import re
from task_1 import read_input

import itertools


def mask(m, addres):
    binVal = format(addres, '036b')
    floating = list()
    
    res = []
    for i, bit in enumerate(m):
        if bit == "0":
            res += binVal[i]
        elif bit == "X":
            floating.append(i)
            res += bit      
        else:
            res += bit

    ret = []
    for combination in list(itertools.product([0, 1], repeat=len(floating))):
        for i, val in enumerate(combination):
            res[floating[i]] = str(val)
        ret.append("".join(res))

    return ret


def writeMemory(data):
    mem = dict()
    i = 0
    for i in data:
        m = i[0].split(" = ")[1]
        for j in i[1:]:
            for add in mask(m, int(re.search("\[(.*?)\]", j).group(1))):
                mem[add] = int(j.split(" = ")[1])

    return mem

def formatInput(inputs):
    data = []
    temp = [inputs[0]]
    for input in inputs[1:]:
        if "mask" in input:
            data.append(temp)
            temp = [input]
        else:
            temp.append(input)

    data.append(temp)
    return data

if __name__ == "__main__":
    data = formatInput(read_input("input.txt"))

    mem = writeMemory(data)

    print(sum(mem.values()))