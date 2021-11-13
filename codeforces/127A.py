from itertools import tee
import math

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

n, k = map(int, input().split())

dist = lambda x1, y1, x2, y2: math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

ps = [list(map(int, input().split())) for _ in range(n)]

total = sum(dist(x1, y1, x2, y2) for [x1, y1], [x2, y2] in pairwise(ps))
print(total / 50 * k)

