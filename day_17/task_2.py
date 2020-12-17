from task_1 import read_input, getInitialState, evolve

if __name__ == "__main__":
    inputs = read_input("input.txt")
    initialState = getInitialState(inputs)
    nDim = 4

    A = initialState.copy()[(...,) + (None,) * (4 - initialState.ndim)]
    for i in range(6):
        A = evolve(A)

    print(A.sum())
