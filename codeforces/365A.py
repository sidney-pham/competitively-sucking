n, k = map(int, input().split())
count = 0
for _ in range(n):
    s = input()
    # This question is stupid and p1 is how I interpreted it as first. 
    p1 = sorted(list(set(s))) == list(str(i) for i in range(k + 1))
    ss = set(s)
    p2 = all(str(i) in ss for i in range(k + 1))
    if p2:
        count += 1
print(count)