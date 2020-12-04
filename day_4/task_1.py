def read_input(filename):
     with open(filename) as f:
         return [str(x) for x in f]

def create_blank_passport():
    return  dict([
        ('byr', None),
        ('iyr', None),
        ('eyr', None),
        ('hgt', None),
        ('hcl', None),
        ('ecl', None),
        ('pid', None),
        ('cid', None)])

def is_valid(passport):
    for key in passport:
        if key == "cid":
            continue
        elif passport[key] == None:
            return False
    return True

inputs =  read_input("input.txt")


seperated = []
data = []

for i, input in enumerate(inputs):
    if(input == "\n"):
        seperated.append("".join(data))
        data = []
    else:
        data.append(input)


count = 0
for info in seperated:
    info = info.replace("\n", " ").split()

    passport = create_blank_passport()

    for values in info:
        values = values.split(":")
        key = values[0]
        val = values[1]
        passport[key] = val

    count += is_valid(passport)

    print(passport)    
    
print(count)


