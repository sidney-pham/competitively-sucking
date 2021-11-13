valid = []
for i in range(3, 10000):
    s = 180 * (i - 2) / i
    if s.is_integer():
        valid.append(int(s))


n = int(input())
for _ in range(n):
    a = int(input())
    print("YES" if a in valid else "NO")