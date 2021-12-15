# Trash.
from heapdict import heapdict

grid = [list(map(int, line.strip())) for line in open("input.txt")]

MAX_X = len(grid[0])
MAX_Y = len(grid)

wrap = lambda x: ((x - 1) % 9) + 1
grid = [
    [
        wrap(grid[y % MAX_Y][x % MAX_X] + (x // MAX_X) + (y // MAX_Y))
        for x in range(MAX_X * 5)
    ]
    for y in range(MAX_Y * 5)
]

MAX_X = len(grid[0]) - 1
MAX_Y = len(grid) - 1


def solve():
    q = heapdict(
        {(x, y): float("inf") for x in range(MAX_X + 1) for y in range(MAX_Y + 1)}
    )
    seen = set()
    start = (0, 0)
    q[start] = 0
    seen.add(start)

    while q:
        v, dist_v = q.popitem()
        if v == (MAX_X, MAX_Y):
            return dist_v
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = v
        for dx, dy in deltas:
            x2 = x + dx
            y2 = y + dy
            v2 = (x2, y2)
            if not (0 <= x2 <= MAX_X and 0 <= y2 <= MAX_Y) or v2 in seen:
                continue
            q[v2] = min(q[v2], dist_v + grid[y2][x2])
        seen.add(v)


print(solve())
