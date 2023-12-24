def print_grid(grid, frame=False):
    grid_width = len(grid[0])
    if frame:
        print("#" * (grid_width + 4))
        print("# " + (" " * grid_width) + " #")
    for line in grid:
        if frame:
            print("# ", end="")
        for char in line:
            print(char, end="")
        if frame:
            print(" #", end="")
        print("\n", end="")
    if frame:
        print("# " + (" " * grid_width) + " #")
        print("#" * (grid_width + 4))


def expand_grid(grid):
    width = len(grid[0])
    columns_to_expand = []
    for x in range(0, width):
        empty = True
        for y in range(0, len(grid)):
            if grid[y][x] == "#":
                empty = False
                break
        if empty:
            columns_to_expand.append(x)
    for i in range(len(columns_to_expand) - 1, -1, -1):
        width += 1
        for row in grid:
            row.insert(columns_to_expand[i], ".")
    row_to_expand = []
    for y in range(0, len(grid)):
        if "#" not in grid[y]:
            row_to_expand.append(y)
    for i in range(len(row_to_expand) - 1, -1, -1):
        grid.insert(row_to_expand[i], [*"." * width])


grid = []
with open("puzzle-input.txt") as file:
    for file_line in file:
        line = file_line.strip()
        grid.append([*line])

expand_grid(grid)

galaxies = []
for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        if grid[y][x] == "#":
            galaxies.append((y, x))

galaxy_pairs = []
for i in range(0, len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        galaxy_pairs.append((galaxies[i], galaxies[j]))

shortest_distance_sum = 0
for pair in galaxy_pairs:
    shortest_distance_sum += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
print(shortest_distance_sum)
