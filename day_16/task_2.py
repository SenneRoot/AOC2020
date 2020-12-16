from task_1 import read_input, formatInput, checkRules
import math


def findValues(yourTicket, nearByTickets, rules):
    possibleFields = {i: set(rules.keys()) for i in range(len(yourTicket))}
    for ticket in nearByTickets:
        if not checkRules(ticket, rules): # returns list of size 0 if valid
            for i, val in enumerate(ticket):
                for k, ranges in rules.items():
                    if val not in ranges[0] and val not in ranges[1]:
                        possibleFields[i].remove(k)

    result = [None for x in possibleFields]

    # sort possible fields on lenght of possible fields
    for input in sorted(possibleFields, key=possibleFields.get):
        result[input] = list(possibleFields[input] - set(result))[0]


    return math.prod([yourTicket[index] for index, dep in enumerate(result) if dep.startswith("departure")])

if __name__ == "__main__":
    rules, yourTicket, nearByTickets = formatInput(read_input("input.txt"))
    
    for nearByTicket in nearByTickets:
       if checkRules(nearByTicket, rules):
           nearByTickets.remove(nearByTicket)
    
    print(findValues(yourTicket, nearByTickets, rules))
