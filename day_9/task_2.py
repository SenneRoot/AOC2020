from task_1 import read_input


def findContiguous(inputs, sumToFind):
    i = 0
    while i < len(inputs):
        sumList = []
        j = i + 1
        sumList.append(inputs[i])
        while j < len(inputs):
            sumList.append(inputs[j])
            if sum(sumList) == sumToFind:
                return sumList
            j += 1
        i += 1
            

if __name__ == "__main__":
    inputs = read_input("input.txt")

    res = findContiguous(inputs, 3199139634)

    print(min(res) + max(res))