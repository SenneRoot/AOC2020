import numpy as np
import collections
from itertools import product


def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]


def pad(origin):
    padded = np.zeros([d + 2 for d in origin.shape], dtype=origin.dtype)
    padded[(slice(1, -1),) * origin.ndim] = origin
    return padded


def countActiveNeighbours(state, position):
    slices = [slice(max(x-1, 0), x+2) for x in position]
    return state[tuple(slices)].sum()


def checkRules(val, neighbursOn):
    result = val
    # rule 1
    result = 1 if not val and neighbursOn == 3 else result
    # rule 2
    result = 0 if val and not neighbursOn in range(3, 5) else result 

    return result


def evolve(origin):
    # pad the array with zero in all dimensions
    origin = pad(origin)
    target = origin.copy()
    # get all positions, star(*) unpacks the list as a positional argument, this is neccaseery for getting the slices for counting the neighbours
    for pos in [*product(*[range(d) for d in origin.shape])]:
        activeNeighbours = countActiveNeighbours(origin, pos)
        target[pos] = checkRules(origin[pos], activeNeighbours)
    return target


def getInitialState(inputs):
    initial = np.zeros((len(inputs), len(inputs[0])), dtype=int)

    for i, row in enumerate(inputs):
        for j, column in enumerate(row):
            if column == "#":
                initial[i, j] = 1

    return initial


if __name__ == "__main__":
    initialState = getInitialState(read_input("input.txt"))
    nDim = 3

    result = initialState.copy()[(...,) + (None,) * (nDim - initialState.ndim)]
    for i in range(6):
        result = evolve(result)

    print(result.sum())
