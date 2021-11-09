grid = [[x for x in input().split()] for _ in range(5)]

for _y in range(5):
    for _x in range(5):
        if grid[_y][_x] == '1':
            y = _y
            x = _x

print(abs(y - 2) + abs(x - 2))