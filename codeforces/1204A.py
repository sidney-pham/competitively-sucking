import math

s = input()
if s == '0':
    print(0)
else:
    l = len(s)
    if s.count('1') == 1:
        print(math.ceil((l - 1) / 2))
    else:
        print(math.ceil(l / 2))


# Doesn't work because math.log(4 ** 49, 4) is the same as math.log(4 ** 49 + 1, 4).
# s = int(input(), base=2)
# if s == 0:
#     print(0)
# else:
#     print(math.ceil(math.log(s, 4)))
