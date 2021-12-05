nums = map(int, input().split(','))

grids = []
while True:
    try:
        blank = input()
    except:
        break
    grid = []
    for _ in range(5):
        grid.append(list(map(int, input().split())))
    grids.append(grid)


def complete(grid):
    def transpose(grid):
        return map(list, zip(*grid))
    def row_complete(grid):
        return any(all(cell is None for cell in row) for row in grid) 
    return row_complete(grid) or row_complete(transpose(grid))

def score(grid):
    return sum(cell for row in grid for cell in row if cell is not None)

completed = 0
for num in nums:
    for grid in grids:
        if complete(grid):
            continue
        for y in range(5):
            for x in range(5):
                if grid[y][x] == num:
                    grid[y][x] = None
        if complete(grid):
            completed += 1
            if completed == len(grids):
                print(score(grid) * num)
                break
    

        