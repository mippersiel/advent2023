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


def expand_grid(grid, value):
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
    for column in columns_to_expand:
        for row in grid:
            row[column] = value
    row_to_expand = []
    for y in range(0, len(grid)):
        if "#" not in grid[y]:
            row_to_expand.append(y)
    for row in row_to_expand:
        grid[row] = [value] * width


def calculate_distance(galaxy_pair, grid):
    [[y1, x1], [y2, x2]] = galaxy_pair
    sum = 0
    if x2 > x1:
        while x1 < x2:
            x1 += 1
            sum += 1 if grid[y1][x1] == "#" else int(grid[y1][x1])
    else:
        while x1 > x2:
            x1 -= 1
            sum += 1 if grid[y1][x1] == "#" else int(grid[y1][x1])
    if y2 > y1:
        while y1 < y2:
            y1 += 1
            sum += 1 if grid[y1][x1] == "#" else int(grid[y1][x1])
    else:
        while y1 > y2:
            y1 -= 1
            sum += 1 if grid[y1][x1] == "#" else int(grid[y1][x1])
    return sum


grid = []
with open("puzzle-input.txt") as file:
    for file_line in file:
        line = file_line.strip()
        grid.append([*line.replace(".", "1")])

expand_grid(grid, "1000000")

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
    shortest_distance_sum += calculate_distance(pair, grid)
print(shortest_distance_sum)
