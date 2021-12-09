grid = [list(map(int, line.strip())) for line in open("input")]

max_y = len(grid) - 1
max_x = len(grid[0]) - 1

total = 0
for y in range(max_y + 1):
    for x in range(max_x + 1):
        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if all(
            grid[y][x] < grid[y + dy][x + dx]
            for dy, dx in deltas
            if 0 <= x + dx <= max_x and 0 <= y + dy <= max_y
        ):
            total += 1 + grid[y][x]

print(total)
