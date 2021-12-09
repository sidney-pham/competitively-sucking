from functools import reduce

grid = [list(map(int, line.strip())) for line in open("input")]

max_y = len(grid) - 1
max_x = len(grid[0]) - 1

sizes = []


def flood_fill(y, x):
    def _flood_fill(y, x):
        if grid[y][x] == 9 or grid[y][x] is None:
            return 0
        grid[y][x] = None
        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        return 1 + sum(
            _flood_fill(y + dy, x + dx)
            for dy, dx in deltas
            if 0 <= x + dx <= max_x and 0 <= y + dy <= max_y
        )

    size = _flood_fill(y, x)
    sizes.append(size)
    return size


for y in range(max_y + 1):
    for x in range(max_x + 1):
        if grid[y][x] is None or grid[y][x] == 9:
            continue
        flood_fill(y, x)

print(reduce(lambda x, y: x * y, sorted(sizes, reverse=True)[:3]))
