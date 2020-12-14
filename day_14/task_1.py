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
            
            mem[addres] = mask(m, value)
            i += 1
        i += 1

    return mem

if __name__ == "__main__":
    mem = writeMemory(read_input("input.txt"))

    print(sum(mem.values()))