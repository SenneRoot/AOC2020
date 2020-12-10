from task_1 import read_input

def findContiguous(inputs, sumToFind):
    for index, i in enumerate(inputs):
        sums = i       
        sumList = list()
        sumList.append(i)
        for j in inputs[index + 1:]:
            sumList.append(j)
            sums += j
            if sums == sumToFind:
                return sumList
    
    return []
            
if __name__ == "__main__":
    res = findContiguous(read_input("input.txt"), 3199139634)

    print(min(res) + max(res))