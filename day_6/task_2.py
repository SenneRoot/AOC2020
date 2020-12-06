from task_1 import read_input


def count_answers(data):
    count = 0
    nPersons = len(data)

    lAnswerMap = {}
    for pers in data:
        for ans in pers.strip("\n"):
            if ans not in lAnswerMap:
                lAnswerMap[ans] = 1
            else:
                lAnswerMap[ans] += 1

    for val in lAnswerMap.values():
        if val == nPersons:
            count += 1

    return count


if __name__ == "__main__":
    inputs = read_input("input.txt")

    data = []
    count = 0
    for input in inputs:
        if input == "\n":
            count += count_answers(data)
            data = []
        else:
            data.append(input)

    print(count)
