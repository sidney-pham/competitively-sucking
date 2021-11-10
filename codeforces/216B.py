from collections import defaultdict

n, m = map(int, input().split())
enemies = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    enemies[a].append(b)
    enemies[b].append(a)

# Answer starts at 0.
# For every odd cycle, add one (since odd cycles can't be 2-coloured.)
# If we end up with an odd number of remaining vertices, add one.

def in_odd_cycle(v, visited):
    seen = set()
    def _in_cycle(v, parent=None):
        if v in seen:
            return True
        if not enemies[v]:
            return False
        seen.add(v)
        visited.add(v)

        res = False
        for w in enemies[v]:
            if w != parent:
                res |= _in_cycle(w, v)
        return res
        # This doesn't work because it short-circuits and we won't visit all the connected nodes.
        # return any(_in_cycle(w, v) for w in enemies[v] if w != parent)

    return _in_cycle(v) and len(seen) % 2 == 1

ans = 0
seen = set()
for i in range(1, n + 1):
    if i in seen:
        continue
    if in_odd_cycle(i, seen):
        ans += 1

if (n - ans) % 2 == 1:
    ans += 1

print(ans)

