tx1 = 281
tx2 = 311
ty1 = -74
ty2 = -54


def fire(v):
    positions = [(0, 0), v]
    pos = v
    x, y = pos
    while x <= tx2 and y >= ty1:
        x, y = pos
        vx, vy = v
        new_vx = 0
        if vx > 0:
            new_vx = vx - 1
        if vx < 0:
            new_vx = vx + 1
        v = (new_vx, vy - 1)
        pos = (x + new_vx, y + vy - 1)
        positions.append(pos)
    return positions


def solve():
    maxes = []
    for y in range(1000):
        for x in range(1000):
            positions = fire((x, y))
            if any(tx1 <= x <= tx2 and ty1 <= y <= ty2 for x, y in positions):
                maxes.append(max(y for _, y in positions))

    return max(maxes)


print(solve())


# Trying too hard.


def gprint(grid):
    for row in grid:
        print("".join(row))


def within(y, x, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def display(positions, max_y, min_y, max_x, tx1, tx2, ty1, ty2):
    grid = [["."] * (max_x + 1) for _ in range(max_y - min_y + 1)]

    for y in range(max_y - ty2, max_y - ty1 + 1):
        for x in range(tx1, tx2 + 1):
            grid[y][x] = "T"

    for i, (x, y) in enumerate(positions):
        y = max_y - y
        if within(y, x, grid):
            if i == 0:
                grid[y][x] = "S"
            else:
                grid[y][x] = "#"
    gprint(grid)


# positions = fire((7, 2))

# ys = list(map(lambda x: x[1], positions))
# xs = list(map(lambda x: x[0], positions))
# display(positions, max(ys), -10, 30, 20, 30, -10, -5)
