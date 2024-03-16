from dataclasses import dataclass

input_file = open('input.txt', 'r')
all_lines = input_file.readlines()


@dataclass
class Node:
    left: str
    right: str


steps = all_lines[0] * 100  # Just a guess

nodes = {}

for i, line in enumerate(all_lines):
    if i > 1:
        line = line.strip().replace("=", "").replace(",", "").replace("(", "").replace(")", "").split()
        nodes[line[0]] = Node(left=line[1], right=line[2])

first_node = nodes["AAA"]
goal = "ZZZ"
steps_taken = 0

for step in steps:
    next_node = ""
    if step == "L":
        next_node = first_node.left
        first_node = nodes[next_node]
        steps_taken = steps_taken + 1
    if step == "R":
        next_node = first_node.right
        first_node = nodes[next_node]
        steps_taken = steps_taken + 1
    if next_node == goal:
        print(str(steps_taken))
        break
