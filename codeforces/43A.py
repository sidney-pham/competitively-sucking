from typing import Counter

from collections import Counter

n = int(input())
goals = []
for _ in range(n):
    goals.append(input())

counter = Counter(goals)
print(max(goals, key=counter.get))