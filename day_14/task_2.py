import re
from task_1 import read_input
import itertools


def mask(m, addres):
    binVal = format(addres, '036b')
    floating = list()

    maskResult = []
    for i, bit in enumerate(m):
        if bit == "0":
            maskResult += binVal[i]
        elif bit == "X":
            floating.append(i)
            maskResult += bit
        else:
            maskResult += bit

    ret = []
    for combination in list(itertools.product([0, 1], repeat=len(floating))):
        for i, val in enumerate(combination):
            maskResult[floating[i]] = str(val)
        ret.append("".join(maskResult))

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
    data = formatInput(read_input("test_input.txt"))

    mem = writeMemory(data)

    print(sum(mem.values()))
