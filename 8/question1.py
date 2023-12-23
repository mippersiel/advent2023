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
count = 0
current_node = "AAA"
while current_node != "ZZZ":
    current_node = nodes[current_node][sequence[idx]]
    count += 1
    idx = 0 if idx == max_idx - 1 else idx + 1

print(count)
