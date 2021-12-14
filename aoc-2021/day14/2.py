import sys
import math
from collections import defaultdict, Counter

polymer = input()

rules = {}
for line in sys.stdin:
    line = line.strip()
    if line:
        l, r = line.split(" -> ")
        rules[l] = r

pair_count = {pair: polymer.count(pair) for pair in rules}

for _ in range(40):
    original_pair_count = dict(pair_count)
    for pair in pair_count:
        a, b = pair
        x = original_pair_count[pair]
        if x == 0:
            continue
        pair_count[pair] -= x
        a1 = a + rules[pair]
        a2 = rules[pair] + b
        pair_count[a1] += x
        pair_count[a2] += x

double_counter = defaultdict(int)
for pair, count in pair_count.items():
    a, b = pair
    double_counter[a] += count
    double_counter[b] += count

counter = defaultdict(int)
for c, x in double_counter.items():
    counter[c] = math.ceil(x / 2)

c = Counter(counter)
print(c.most_common()[0][1] - c.most_common()[-1][1])
