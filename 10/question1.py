import sys


sys.setrecursionlimit(1000000)


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


def navigate_coordinate(grid, current_location, count, last_location):
    max_x = len(grid[0])
    max_y = len(grid)
    y = current_location[0]
    x = current_location[1]
    if grid[y][x] == "S" and count != 0:
        return count
    elif (
        x > 0
        and connects_to_left(grid, (y, x))
        and connects_to_right(grid, (y, x - 1))
        and last_location != (y, x - 1)
    ):
        return navigate_coordinate(
            grid,
            (y, x - 1),
            count + 1,
            current_location,
        )
    elif (
        y < max_y - 1
        and connects_to_bottom(grid, (y, x))
        and connects_to_top(grid, (y + 1, x))
        and last_location != (y + 1, x)
    ):
        return navigate_coordinate(
            grid,
            (y + 1, x),
            count + 1,
            current_location,
        )
    elif (
        x < max_x - 1
        and connects_to_right(grid, (y, x))
        and connects_to_left(grid, (y, x + 1))
        and last_location != (y, x + 1)
    ):
        return navigate_coordinate(
            grid,
            (y, x + 1),
            count + 1,
            current_location,
        )
    elif (
        y > 0
        and connects_to_top(grid, (y, x))
        and connects_to_bottom(grid, (y - 1, x))
        and last_location != (y - 1, x)
    ):
        return navigate_coordinate(
            grid,
            (y - 1, x),
            count + 1,
            current_location,
        )
    else:
        print("ERROR")
        exit()


grid = []
start_x = -1
start_y = -1
with open("puzzle-input.txt") as file:
    for file_line in file:
        line = file_line.strip()
        if "S" in line:
            start_x = line.index("S")
            start_y = len(grid)
        grid.append([*line])
count = navigate_coordinate(grid, (start_y, start_x), 0, (-1, -1))
print(int(count / 2))
