import re
from dataclasses import dataclass

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()


@dataclass(frozen=True)
class Node:
    left: str
    right: str


steps = all_lines[0] * 10000000  # Just a big number, since smaller ones did not work

nodes = {}

for i, line in enumerate(all_lines):
    if i > 1:
        line = line.strip().replace("=", "").replace(",", "").replace("(", "").replace(")", "").split()
        nodes[line[0]] = Node(left=line[1], right=line[2])

starting_nodes = []
for node in nodes:
    if re.match("\w\wA", node):
        starting_nodes.append(node)
goal = re.compile(r"\w\wZ")
steps_taken = 0

for step in steps:
    next_nodes = []
    if step == "L":
        for node in starting_nodes:
            node = nodes[node]
            next_nodes.append(node.left)
        starting_nodes = next_nodes
        steps_taken = steps_taken + 1
    if step == "R":
        for node in starting_nodes:
            node = nodes[node]
            next_nodes.append(node.right)
        starting_nodes = next_nodes
        steps_taken = steps_taken + 1
    all_match = list(filter(goal.search, starting_nodes))
    if len(all_match) == len(starting_nodes):
        print(str(steps_taken))
        break
