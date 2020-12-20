import re

def convert(matchobj):
    return f"TheSpecialOne({matchobj.group(0)})"
    
class TheSpecialOne(int):
    def __add__(self, other):
        return TheSpecialOne(int(self) + int(other))

    def __sub__(self, other):
        return TheSpecialOne(self * other)

    @staticmethod
    def eval(expr):
        # relace the ints with our special ones to handle the evaluation, we replace the operators to follow the rules
        converted = re.sub("\d+", convert, expr.replace("*", "-"))
        return eval(converted)

def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]

if __name__ == "__main__":
    inputs = read_input("input.txt")

    t = map(TheSpecialOne.eval, inputs)
    print("Part 1:", sum(t))



