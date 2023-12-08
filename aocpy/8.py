import math
import os
import re

from aocpy.shared import INPUTS_DIR, timer


@timer
def solve():
    # Part #1
    with open(os.path.join(INPUTS_DIR, "day8.txt")) as f:
        directions = [l for line in f.readlines() if (l := line.strip()) != ""]
    instructions = directions[0]
    network = {}
    for node_connections in directions[1:]:
        node, connections = node_connections.split(" = ")
        left, right = re.findall(r"(\w+)", connections)
        network[node] = {"L": left, "R": right}

    def _next_instruction(instructions):
        next_i = 0
        while True:
            next_i = 0 if next_i >= len(instructions) else next_i
            yield instructions[next_i]
            next_i += 1

    current_node = "AAA"
    steps = 0
    for next_instruction in _next_instruction(instructions):
        current_node = network[current_node][next_instruction]
        steps += 1
        if current_node == "ZZZ":
            break

    print(f"Answer #1: {steps}")
    assert steps == 12599

    # Part #2
    current_nodes = [node for node in network.keys() if node.endswith("A")]
    steps = []
    steps_i = 0
    for next_instruction in _next_instruction(instructions):
        current_nodes = [
            network[current_node][next_instruction]
            for current_node in current_nodes
        ]
        steps_i += 1
        nodes_z_ending = [n for n in current_nodes if n.endswith("Z")]
        if len(nodes_z_ending) > 0:
            for n in nodes_z_ending:
                steps.append(steps_i)
                current_nodes.remove(n)
        if len(current_nodes) == 0:
            break
    print(f"Answer #2: {math.lcm(*steps)}")
    assert math.lcm(*steps) == 8245452805243
