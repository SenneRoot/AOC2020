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
        temp = res.copy()
        for i, val in enumerate(combination):
            temp[floating[i]] = str(val)
        ret.append("".join(temp))


    return ret


def writeMemory(inputs):
    mem = dict()
    i = 0
    while i < len(inputs):
        m = inputs[i].split(" = ")[1]
        for input in inputs[i + 1:]:
            if "mask" in input:
                break
            addres = int(re.search("\[(.*?)\]", input).group(1))
            value = int(input.split(" = ")[1])
            
            for add in mask(m, addres):
                mem[add] = value
            i += 1
        i += 1

    return mem

if __name__ == "__main__":
    mem = writeMemory(read_input("input.txt"))

    print(sum(mem.values()))