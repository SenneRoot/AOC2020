import re

eye_colors = [
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth']


def checkBYR(byr):
    if int(byr) < 1920 or int(byr) > 2002:
        print("Wrong byr: " + byr)
        return False
    return True


def checkIYR(iyr):
    if int(int(iyr)) < 2010 or int(iyr) > 2020:
        print("Wrong iyr: " + iyr)
        return False
    return True


def checkEYR(eyr):
    if int(eyr) < 2020 or int(eyr) > 2030:
        print("Wrong eyr: " + eyr)
        return False
    return True


def checkECL(ecl):
    if any(ecl in s for s in eye_colors):
        return True
    else:
        print("Wrong ecl: " + ecl)
        return False


def checkHeight(height):
    suffix = height[-2:]
    if suffix != "cm" and suffix != "in":
        return False

    if(suffix == "cm"):
        try:
            return int(height[0:3]) >= 150 and int(height[0:3]) <= 193
        except ValueError:
            print("Wrong hgt: " + height)
            return False
    elif(suffix == "in"):
        try:
            return int(height[0:2]) >= 59 and int(height[0:2]) <= 76
        except ValueError:
            print("Wrong hgt: " + height)
            return False


def checkHCL(hcl):
    if re.match("(^#[0-9a-fA-F]{6})", hcl):
        return True
    else:
        print("Wrong hcl: " + hcl)
        return False


def checkPID(pid):
    if re.match("^\d{9}$", pid):
        return True
    else:
        print("Wrong pid: " + pid)
        return False


funct = {
    "byr": checkBYR,
    "iyr": checkIYR,
    "eyr": checkEYR,
    "hgt": checkHeight,
    "hcl": checkHCL,
    "ecl": checkECL,
    "pid": checkPID
}


def is_valid(passport):
    for key in passport:
        if passport[key] == None and key != "cid":
            return False
        elif key == "cid":
            continue
        else:
            if not funct[key](passport[key]):
                return False

    return True


def create_blank_passport():
    return dict([
        ('byr', None),
        ('iyr', None),
        ('eyr', None),
        ('hgt', None),
        ('hcl', None),
        ('ecl', None),
        ('pid', None),
        ('cid', None)])


def read_input(filename):
    with open(filename) as f:
        return [str(x) for x in f]


inputs = read_input("input.txt")
formatted = []

data = []
for i, input in enumerate(inputs):
    if(input == "\n"):
        formatted.append("".join(data))
        data = []
    else:
        data.append(input)

count = 0
for info in formatted:
    info = info.replace("\n", " ").split()

    passport = create_blank_passport()

    for values in info:
        values = values.split(":")
        key = values[0]
        val = values[1]
        passport[key] = val

    count += is_valid(passport)

print(count)
