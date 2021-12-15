grid = [list(map(int, line.strip())) for line in open("input.txt")]

MAX_X = len(grid[0]) - 1
MAX_Y = len(grid) - 1


def solve():
    dist = {(x, y): float("inf") for x in range(MAX_X + 1) for y in range(MAX_Y + 1)}
    seen = set()
    start = (0, 0)
    dist[start] = 0
    seen.add(start)
    q = sorted(dist.keys(), key=dist.get)
    while q:
        v = q.pop(0)
        if v == (MAX_X, MAX_Y):
            return dist[v]
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = v
        for dx, dy in deltas:
            x2 = x + dx
            y2 = y + dy
            v2 = (x2, y2)
            if not (0 <= x2 <= MAX_X and 0 <= y2 <= MAX_Y) or v2 in seen:
                continue
            dist[v2] = min(dist[v2], dist[v] + grid[y2][x2])
        seen.add(v)
        q.sort(key=dist.get)


print(solve())
