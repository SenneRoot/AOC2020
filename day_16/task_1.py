def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]

def formatInput(inputs):
    rules = dict()
    yourTicket = list()
    nearByTickets = list()

    i = 0
    while inputs[i] != "":
        rule, ranges = inputs[i].split(":")
        temp = []
        for r in ranges.split(" or "):
            rStart, rStop = r.split("-")
            temp.append(range(int(rStart), int(rStop) + 1))
        rules[rule] = temp
        i += 1

    i = inputs.index("your ticket:") + 1
    yourTicket = [int(i) for i in inputs[i].split(",")]

    i = inputs.index("nearby tickets:") + 1
    while inputs[i] != "":
        nearByTickets.append([int(i) for i in inputs[i].split(",")])
        i += 1

    return rules, yourTicket, nearByTickets

def checkRules(ticket, rules):
    notValid = []
    for val in ticket:
        found = False
        for ranges in rules.values():
            if val in ranges[0] or val in ranges[1]:
                found = True
        if found == False:
            notValid.append(val)

    return notValid

if __name__ == "__main__":
    rules, yourTicket, nearByTickets = formatInput(read_input("input.txt"))
    
    tser = 0
    for nearByTicket in nearByTickets:
        tser += sum(checkRules(nearByTicket, rules))
    
    print(tser)
