import math
n = int(input())
a = list(int(input()) for _ in range(n))

pos_last = False
for b in a:
    if b % 2 == 0:
        print(b // 2)
    else:
        print(math.floor(b / 2) if pos_last else math.ceil(b / 2))
        pos_last = not pos_last


# -3.5 -> -3 (+)
# -14.5 -> -15 (-)
# 0 -> 0
# 1.5 -> (+)
# 12 -> 0
# -14.5 -> (-)
# 19 -> 0

