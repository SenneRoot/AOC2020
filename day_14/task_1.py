import re

def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]


def mask(m, value):
    binVal = format(value, '036b')
    
    ret = ""
    for i, bit in enumerate(m):
        if bit == "X":
            ret += binVal[i]
        else:
            ret += bit

    return int(ret, 2)


def writeMemory(data):
    mem = dict()
    i = 0
    for i in data:
        m = i[0].split(" = ")[1]
        for j in i[1:]:
            mem[int(re.search("\[(.*?)\]", j).group(1))] = mask(m, int(j.split(" = ")[1]))

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
