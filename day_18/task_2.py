from task_1 import read_input
import re

def convert(matchobj):
    return f"TheSecondSpecialOne({matchobj.group(0)})"
    
class TheSecondSpecialOne(int):
    def __add__(self, other):
        return TheSecondSpecialOne(int(self) * int(other))

    def __mul__(self, other):
        return TheSecondSpecialOne(int(self) + int(other))

    @staticmethod
    def eval(expr):
        # relace the ints with our special ones to handle the evaluation, we replace the operators to follow the rules
        converted = re.sub("\d+", convert, expr.replace("+", "x").replace("*", "+").replace("x", "*"))
        return eval(converted)

if __name__ == "__main__":
    inputs = read_input("input.txt")

    mappedExpressions = map(TheSecondSpecialOne.eval, inputs)
    print("Part 2:", sum(mappedExpressions)) 
