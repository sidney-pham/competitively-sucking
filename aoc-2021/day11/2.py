grid = [list(map(int, line.strip())) for line in open('input.txt')]

def iterate(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            yield y, x, grid[y][x]

to_reset = set()
def any_flashable(grid):
    return any(cell > 9 and (y, x) not in to_reset for y, x, cell in iterate(grid))

def all_zeros(grid):
    return all(cell == 0 for _, _, cell in iterate(grid))

step = 0
while not all_zeros(grid):
    to_reset = set()
    for y, x, _ in iterate(grid):
        grid[y][x] += 1

    while any_flashable(grid):
        for y, x, cell in iterate(grid):
            if cell > 9 and (y, x) not in to_reset:
                to_reset.add((y, x))
                deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                for dy, dx in deltas:
                    if 0 <= y + dy <= len(grid) - 1 and 0 <= x + dx <= len(grid[0]) - 1:
                        grid[y + dy][x + dx] += 1

    for y, x in to_reset:
        grid[y][x] = 0
    
    step += 1

print(step)