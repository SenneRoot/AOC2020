from task_1 import read_input


def count_answers(data):
    count = 0
    nPersons = len(data)

    answerMap = {}
    for pers in data:
        for char in pers.strip("\n"):
            if char not in answerMap:
                answerMap[char] = 1
            else:
                answerMap[char] += 1

    for val in answerMap.values():
        if val == nPersons:
            count += 1

    return count


if __name__ == "__main__":
    data = []
    count = 0
    for input in read_input("input.txt"):
        if input == "\n":
            count += count_answers(data)
            data = []
        else:
            data.append(input)

    print(count)
