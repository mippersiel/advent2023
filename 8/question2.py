from math import lcm


sequence = []
nodes = {}
with open("puzzle-input.txt") as file:
    for file_line in file:
        line = file_line.strip()
        if not line:
            continue

        if "=" in line:
            [start, node_entries] = line.split(" = ")
            [left, right] = node_entries[1:-1].split(", ")
            nodes[start] = {"L": left, "R": right}
        else:
            sequence = [*line]

max_idx = len(sequence)
idx = 0
starting_nodes = []
for node in nodes:
    if node[-1] == "A":
        starting_nodes.append(node)

loop_cycles = []
for current_node in starting_nodes:
    count = 0
    hits = []
    finished = False
    while not finished:
        count += 1
        current_node = nodes[current_node][sequence[idx]]
        if current_node[-1] == "Z":
            hit_entry = {"node": current_node, "count": count}
            for hit in hits:
                if hit["node"] == hit_entry["node"]:
                    count = hit["count"]
                    finished = True
            if not finished:
                hits.append(hit_entry)
        idx = 0 if idx == max_idx - 1 else idx + 1
    loop_cycles.append(count)

print(lcm(*loop_cycles))
