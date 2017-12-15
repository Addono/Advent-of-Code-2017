from math import sqrt, floor

input = 312051

# Compute the width of the inner square, which is the largest odd integer which squared value is smaller than the input.
width_inner_square = 2 * floor(sqrt(input) / 2)

# Consider the outer row,
position_on_outer_row = input - width_inner_square ** 2
position_on_edge = position_on_outer_row % (width_inner_square + 1)

distance = abs(position_on_edge - (width_inner_square // 2)) + (width_inner_square // 2)

print("Part 1: " + str(distance))


def grid_has(grid: dict, x: int, y: int) -> bool:
    if x in grid:
        if y in grid.get(x):
            return True
    return False


def grid_get(grid: dict, x: int, y: int) -> int:
    if not grid_has(grid, x, y):
        return 0
    else:
        return grid.get(x).get(y)


def grid_set(grid: dict, x: int, y: int, value: int):
    grid[x][y] = value


def grid_calculate(grid: dict, x: int, y: int):
    amount = grid_get(grid, x - 1, y) + grid_get(grid, x + 1, y)
    for i in range(-1, 2):
        amount += grid_get(grid, x + i, y - 1) + grid_get(grid, x + i, y + 1)

    return amount


def compute_coordinates(i: int) -> list:
    # Compute the width of the inner square, which is the largest odd integer which squared value is smaller than the input.
    width_inner_square = 2 * floor(sqrt(i) / 2)

    # Consider the outer row,
    position_on_outer_row = i - width_inner_square ** 2
    position_on_edge = position_on_outer_row % (width_inner_square + 1)
    edge = position_on_outer_row // (width_inner_square + 1)

g = {0: {0: 1}}

prev = 0
count = 1
while prev <= input:
    count += 1
