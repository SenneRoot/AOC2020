from task_1 import read_input

def countArrangements(lines):
    adapters = sorted(lines)
    # possible path to zero is always 1, else there will be no paths to the other adapters
    paths = {0 : 1}
    # for every adapter count the possible ways to get to that adapter by adding the possible ways to get to the previous adapter
    for adapter in adapters:
        if adapter in paths:
            paths[adapter] += sum(paths[i] for i in range(adapter - 3, adapter) if i in paths)
        else:
            paths[adapter] = sum(paths[i] for i in range(adapter - 3, adapter) if i in paths)
    return paths[adapters[-1]]


if __name__ == "__main__":
    print(countArrangements(read_input("input.txt")))
