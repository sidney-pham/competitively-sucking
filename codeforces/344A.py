from itertools import groupby

n = int(input())
gs = [input() for _ in range(n)]

print(len(list(groupby(gs))))