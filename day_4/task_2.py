import re


def checkBYR(byr):
    if re.match("^(19[2-9][0-9]|200[0-2])$", byr):
        return True
    else:
        print("Wrong byr: " + byr)
        return False


def checkIYR(iyr):
    if re.match("^(201[0-9]|2020)$", iyr):
        return True
    else:
        print("Wrong iyr: " + iyr)
        return False


def checkEYR(eyr):
    if re.match("^(202[0-9]|2030)$", eyr):
        return True
    else:
        print("Wrong eyr: " + eyr)
        return False


def checkECL(ecl):
    if re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", ecl):
        return True
    else:
        print("Wrong ecl: " + ecl)
        return False


def checkHeight(hgt):
    if re.match("((1[5-8][0-9]|19[0-3])cm|^(59|6[0-9]|7[0-6])in)$", hgt):
        return True
    else:
        print("Wrong hgt: " + hgt)
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


validate = {
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
            if not validate[key](passport[key]):
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
count = 0
for i, input in enumerate(inputs):
    if(input == "\n"):
        info = "".join(data).replace("\n", " ").split()
        passport = create_blank_passport()

        for values in info:
            values = values.split(":")
            passport[values[0]] = values[1]

        count += is_valid(passport)
        data.clear()
    else:
        data.append(input)

print(count)
