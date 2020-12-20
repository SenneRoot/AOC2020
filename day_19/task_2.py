from collections import deque 
import networkx as nx
import regex
from task_1 import read_input, formatData, add_rule, resolve

if __name__ == "__main__":
    inputs = read_input("input.txt")

    rules, input = formatData(inputs)

    graph = nx.DiGraph()

    for rule in rules:
        # Skip rules 0, 8, and 11; we manually handle those because of an endless loop
        # 0 only contains 8 an 11 so we need to also skip that one
        graph = add_rule(graph, rule, skip={'0', '8', '11'})

    resolve(graph)

    rule_31 = graph.nodes['31']['rule']
    rule_42 = graph.nodes['42']['rule']

    # Use a recursive regex here
    rule_0 = fr'(?:{rule_42})+((?:{rule_42})(|(?1))(?:{rule_31}))'
    print(len([message for message in input if regex.fullmatch(rule_0, message)]))



       


