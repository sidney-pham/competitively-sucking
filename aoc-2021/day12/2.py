from collections import defaultdict

graph = defaultdict(list)
for line in open("input.txt"):
    u, v = line.strip().split("-")
    graph[u].append(v)
    graph[v].append(u)


def solve(start, end):
    def _solve(start, end, can_visit_twice, small_visited):
        if start == end:
            return [[start]]
        paths = []
        for v in graph[start]:
            if v == "start":
                continue
            if v != can_visit_twice and v in small_visited:
                continue
            if v in small_visited and small_visited[v] >= 2:
                continue
            new_small_visited = small_visited.copy()
            if start.islower():
                new_small_visited[start] = small_visited.get(start, 0) + 1
            for path in _solve(v, end, can_visit_twice, new_small_visited):
                paths.append([start] + path)

        return paths

    out = []
    for v in graph.keys():
        if v.islower() and v not in ["start", "end"]:
            out += _solve(start, end, v, {})
    return list(set(map(tuple, out)))


res = solve("start", "end")
for path in res:
    print(",".join(path))

print(len(res))
