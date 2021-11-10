n = int(input())
ns = list(map(int, input().split()))

# print(' '.join(str(ns.index(i) + 1) for i in range(1, n + 1)))

out = [None] * n
for i, x in enumerate(ns, 1):
    out[x - 1] = i
print(' '.join(map(str, out)))