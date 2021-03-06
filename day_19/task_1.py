from collections import deque 
import networkx as nx
import re

import matplotlib.pyplot as plt

def add_rule(graph, rule, skip=None):
    number, rule = rule.split(':')

    if skip and number in skip:
        return graph

    rule = rule.strip().split(' ')

    # handle a or b
    if re.search("[ab]", rule[0]):
        # Remove quotes for leaf nodes
        graph.add_node(number, rule=rule[0].strip('"'))
    else:
        graph.add_node(number, rule=rule)

        # For each dependency in the rule, add a directed edge
        # from the dependency to the rule
        for term in rule:
            if term != '|':
                graph.add_edge(term, number)

    return graph


def resolve(graph):
    # Resolve the rules in the graph by iterating through a topologically sorted
    # list of the nodes, so that dependencies are resolved first
    for node in nx.topological_sort(graph):
        rule = graph.nodes[node]['rule']
        if isinstance(rule, list):
            for i, term in enumerate(rule):
                if term != '|':
                    term_rule = graph.nodes[term]['rule']
                    rule[i] = fr'(?:{term_rule})'

            graph.nodes[node]['rule'] = ''.join(rule)




def read_input(filename):
    return [str(x).rstrip() for x in open(filename)]

def formatData(inputs):
    rules = inputs[:inputs.index("")]
    input = inputs[inputs.index("")+1:]


    return rules, input

if __name__ == "__main__":
    inputs = read_input("input.txt")

    rules, input = formatData(inputs)

    graph = nx.DiGraph()

    for rule in rules:
        graph = add_rule(graph, rule)

    resolve(graph)

    rule_0 = graph.nodes['0']['rule']
    t = [message for message in input if re.fullmatch(rule_0, message)]
    print(len([message for message in input if re.fullmatch(rule_0, message)]))


    nx.draw(graph,with_labels=True)
    plt.draw()
    plt.show()

       


