import sys
from itertools import tee
from collections import Counter


def pairwise(xs):
    a, b = tee(xs)
    next(b, None)

    return zip(a, b)


polymer = input()

rules = {}
for line in sys.stdin:
    line = line.strip()
    if line:
        l, r = line.split(" -> ")
        rules[l] = r


for _ in range(10):
    out = polymer[0]
    for a, b in pairwise(polymer):
        pair = "".join((a, b))
        if pair in rules:
            out += rules[pair]
        out += b
    polymer = out


c = Counter(polymer)
print(c.most_common()[0][1] - c.most_common()[-1][1])
