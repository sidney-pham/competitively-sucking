from collections import defaultdict

graph = defaultdict(list)
for line in open("input3.txt"):
    u, v = line.strip().split("-")
    graph[u].append(v)
    graph[v].append(u)


def solve(start, end):
    def _solve(start, end, small_visited):
        if start == end:
            return [[start]]
        paths = []

        for v in graph[start]:
            if v in small_visited:
                continue
            for path in _solve(
                v, end, small_visited.union({start} if start.islower() else {})
            ):
                paths.append([start] + path)
        return paths

    return _solve(start, end, set())


res = solve("start", "end")
for path in res:
    print(",".join(path))

print(len(res))
