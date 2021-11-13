l, r = map(int, input().split())

def gcd(a, b):
    def _gcd(a, b):
        if b == 0:
            return a
        return _gcd(b, a % b)
    return _gcd(min(a, b), max(a, b))


for a in range(l, r + 1):
    for b in range(a + 1, r + 1):
        for c in range(b + 1, r + 1):
            if gcd(a, b) == 1 and gcd(b, c) == 1 and gcd(a, c) != 1:
                print(a, b, c)
                break
        else:
            continue
        break
    else:
        continue
    break
else:
    print(-1)