def connects_to_bottom(grid, grid_coordinates):
    y = grid_coordinates[0]
    x = grid_coordinates[1]
    item = grid[y][x]
    if item == "|" or item == "7" or item == "F" or item == "S":
        return True
    else:
        return False


def connects_to_left(grid, grid_coordinates):
    y = grid_coordinates[0]
    x = grid_coordinates[1]
    item = grid[y][x]
    if item == "-" or item == "J" or item == "7" or item == "S":
        return True
    else:
        return False


def connects_to_top(grid, grid_coordinates):
    y = grid_coordinates[0]
    x = grid_coordinates[1]
    item = grid[y][x]
    if item == "|" or item == "L" or item == "J" or item == "S":
        return True
    else:
        return False


def connects_to_right(grid, grid_coordinates):
    y = grid_coordinates[0]
    x = grid_coordinates[1]
    item = grid[y][x]
    if item == "-" or item == "L" or item == "F" or item == "S":
        return True
    else:
        return False


def start_equivalent_symbol(y, x, grid):
    max_x = len(grid[0])
    max_y = len(grid)
    left = False
    right = False
    top = False
    bottom = False
    if x > 0 and connects_to_right(grid, (y, x - 1)):
        left = True
    if y < max_y - 1 and connects_to_top(grid, (y + 1, x)):
        bottom = True
    if x < max_x - 1 and connects_to_left(grid, (y, x + 1)):
        right = True
    if y > 0 and connects_to_bottom(grid, (y - 1, x)):
        top = True

    if top:
        if bottom:
            return "|"
        elif right:
            return "L"
        elif left:
            return "J"
    elif bottom:
        if top:
            return "|"
        elif right:
            return "F"
        elif left:
            return "7"
    elif right:
        if top:
            return "L"
        elif bottom:
            return "F"
        elif left:
            return "-"
    elif left:
        if top:
            return "J"
        elif bottom:
            return "7"
        elif right:
            return "-"


def write_pixel_grid(center_y, center_x, pixel_grid, symbol):
    pipe_symbol = "#"

    if symbol == "|":
        pixel_grid[center_y - 1][center_x] = pipe_symbol
        pixel_grid[center_y][center_x] = pipe_symbol
        pixel_grid[center_y + 1][center_x] = pipe_symbol
    elif symbol == "-":
        pixel_grid[center_y][center_x - 1] = pipe_symbol
        pixel_grid[center_y][center_x] = pipe_symbol
        pixel_grid[center_y][center_x + 1] = pipe_symbol
    elif symbol == "7":
        pixel_grid[center_y][center_x - 1] = pipe_symbol
        pixel_grid[center_y][center_x] = pipe_symbol
        pixel_grid[center_y + 1][center_x] = pipe_symbol
    elif symbol == "F":
        pixel_grid[center_y][center_x + 1] = pipe_symbol
        pixel_grid[center_y][center_x] = pipe_symbol
        pixel_grid[center_y + 1][center_x] = pipe_symbol
    elif symbol == "L":
        pixel_grid[center_y][center_x + 1] = pipe_symbol
        pixel_grid[center_y][center_x] = pipe_symbol
        pixel_grid[center_y - 1][center_x] = pipe_symbol
    elif symbol == "J":
        pixel_grid[center_y][center_x - 1] = pipe_symbol
        pixel_grid[center_y][center_x] = pipe_symbol
        pixel_grid[center_y - 1][center_x] = pipe_symbol
    else:
        print("ERROR in write_pixel_grid")
        exit()


def populate_pixel_grid(y, x, grid, pixel_grid):
    xx = x * 3 + 1
    yy = y * 3 + 1

    if grid[y][x] == "S":
        symbol = start_equivalent_symbol(y, x, grid)
        write_pixel_grid(yy, xx, pixel_grid, symbol)
    else:
        write_pixel_grid(yy, xx, pixel_grid, grid[y][x])


def traverse_pipe_grid(grid, current_location, clean_grid, pixel_grid):
    max_x = len(grid[0])
    max_y = len(grid)
    last_location = (-1, -1)

    at_start = False
    while not at_start:
        y = current_location[0]
        x = current_location[1]
        symbol = grid[y][x]
        clean_grid[y][x] = symbol
        populate_pixel_grid(y, x, grid, pixel_grid)

        if (
            x > 0
            and connects_to_left(grid, (y, x))
            and connects_to_right(grid, (y, x - 1))
            and last_location != (y, x - 1)
        ):
            last_location = current_location
            current_location = (y, x - 1)
        elif (
            y < max_y - 1
            and connects_to_bottom(grid, (y, x))
            and connects_to_top(grid, (y + 1, x))
            and last_location != (y + 1, x)
        ):
            last_location = current_location
            current_location = (y + 1, x)
        elif (
            x < max_x - 1
            and connects_to_right(grid, (y, x))
            and connects_to_left(grid, (y, x + 1))
            and last_location != (y, x + 1)
        ):
            last_location = current_location
            current_location = (y, x + 1)
        elif (
            y > 0
            and connects_to_top(grid, (y, x))
            and connects_to_bottom(grid, (y - 1, x))
            and last_location != (y - 1, x)
        ):
            last_location = current_location
            current_location = (y - 1, x)
        else:
            print("ERROR in traverse_pipe_grid")
            exit()

        at_start = grid[current_location[0]][current_location[1]] == "S"


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


def is_pixel_valid(pixel, pixel_grid):
    max_x = len(pixel_grid[0])
    max_y = len(pixel_grid)
    [y, x] = pixel
    if y == 0 or x == 0 or y == max_y - 1 or x == max_x - 1:
        raise ValueError("Flooding to boundary of grid - bad starting point")

    return pixel_grid[y][x] == " "


def flood_fill(pixel_grid, starting_point):
    queue = []
    queue.append(starting_point)
    flood_symbol = "#"

    while queue:
        [y, x] = queue.pop()
        pixel_grid[y][x] = flood_symbol

        if is_pixel_valid((y + 1, x), pixel_grid):
            queue.append((y + 1, x))
        if is_pixel_valid((y - 1, x), pixel_grid):
            queue.append((y - 1, x))
        if is_pixel_valid((y, x + 1), pixel_grid):
            queue.append((y, x + 1))
        if is_pixel_valid((y, x - 1), pixel_grid):
            queue.append((y, x - 1))


def fill_pixel_grid(start_y, start_x, start_symbol, pixel_grid):
    x = start_x * 3 + 1
    y = start_y * 3 + 1
    starting_points = []

    match start_symbol:
        case "|":
            starting_points.append((y, x - 1))
            starting_points.append((y, x + 1))
        case "-":
            starting_points.append((y - 1, x))
            starting_points.append((y + 1, x))
        case "7":
            starting_points.append((y + 1, x - 1))
            starting_points.append((y - 1, x))
        case "J":
            starting_points.append((y - 1, x - 1))
            starting_points.append((y + 1, x))
        case "L":
            starting_points.append((y - 1, x + 1))
            starting_points.append((y + 1, x))
        case "F":
            starting_points.append((y + 1, x + 1))
            starting_points.append((y - 1, x))
        case _:
            print("ERROR in count_contained_tiles")
            exit()

    backup = []
    for i in range(0, len(pixel_grid)):
        backup.append(pixel_grid[i].copy())
    for starting_point in starting_points:
        try:
            flood_fill(pixel_grid, starting_point)
            break
        except Exception:
            pixel_grid = []
            for i in range(0, len(backup)):
                pixel_grid.append(backup[i].copy())
    return pixel_grid


grid = []
clean_grid = []
pixel_grid = []
start_x = -1
start_y = -1
with open("puzzle-input.txt") as file:
    for file_line in file:
        line = file_line.strip()
        if "S" in line:
            start_x = line.index("S")
            start_y = len(grid)
        grid.append([*line])
        clean_grid.append([*"." * len(line)])
        pixel_grid.append([*" " * len(line) * 3])
        pixel_grid.append([*" " * len(line) * 3])
        pixel_grid.append([*" " * len(line) * 3])

# print_grid(grid)
traverse_pipe_grid(grid, (start_y, start_x), clean_grid, pixel_grid)
# print("")
# print_grid(clean_grid)
# print_grid(pixel_grid)

pixel_grid = fill_pixel_grid(
    start_y, start_x, start_equivalent_symbol(start_y, start_x, grid), pixel_grid
)
# print_grid(pixel_grid)

tile_count = 0
y = 0
for row in clean_grid:
    x = 0
    for symbol in row:
        xx = x * 3 + 1
        yy = y * 3 + 1
        if symbol == "." and pixel_grid[yy][xx] == "#":
            tile_count += 1
        x += 1
    y += 1
print(tile_count)
