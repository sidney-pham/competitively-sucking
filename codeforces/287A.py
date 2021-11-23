grid = [list(input()) for _ in range(4)]

def passes(grid):
    for i in range(3):
        for j in range(3):
            cell = grid[i][j]
            deltas = [(0, 0), (0, 1), (1, 0), (1, 1)]
            if all(grid[i + di][j + dj] == cell for di, dj in deltas):
                return True
    return False

flip = lambda x: '#' if x == '.' else '.'

def solve():
    for i in range(4):
        for j in range(4):
            grid[i][j] = flip(grid[i][j])
            if passes(grid):
                return 'YES'
            grid[i][j] = flip(grid[i][j])
    return 'NO'

print(solve())


