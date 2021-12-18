import math
import sys

sys.setrecursionlimit(99999999)


MARKER = float("inf")


def explode(n):
    exploded = False

    def _propagate_r(n, dl):
        l, r = n
        if type(r) == int:
            return [l, r + dl]
        return [l, _propagate_r(r, dl)]

    def _explode(n, depth, carry_l=0, carry_r=0):
        l, r = n
        if type(l) == int:
            l += carry_r
            carry_r = 0
        if type(r) == int:
            r += carry_l
            carry_l = 0

        if depth == 4:
            nonlocal exploded
            if not exploded:
                exploded = True
                return [MARKER, MARKER], (l, r)
            return [l, r], (0, 0)
        if type(l) != int:
            l, (dl, dr) = _explode(l, depth + 1, carry_l=carry_l, carry_r=carry_r)
            if type(r) == int:
                return [l, r + dr], (dl, 0)
            r, (dl2, dr) = _explode(r, depth + 1, carry_r=dr)
            if dl2 != 0 and type(l) != int:
                return [_propagate_r(l, dl2), r], (dl, dr)
            return [l, r], (dl, dr)

        if type(r) != int:
            r, (dl, dr) = _explode(r, depth + 1)
            return [l + dl, r], (0, dr)

        return [l, r], (0, 0)

    # I don't know how to get remove a node while processing it so I marked it for deletion in a
    # separate pass.
    def _clean(n):
        l, r = n
        if l == [MARKER, MARKER]:
            return [0, r]
        elif r == [MARKER, MARKER]:
            return [l, 0]

        if type(l) == int:
            if type(r) == int:
                return [l, r]
            return [l, _clean(r)]
        if type(r) == int:
            return [_clean(l), r]
        return [_clean(l), _clean(r)]

    res = _explode(n, 0)
    if exploded:
        t = res[0]
        return _clean(t)
    return None


def split(n):
    l, r = n
    if type(l) == int:
        if l >= 10:
            return [[math.floor(l / 2), math.ceil(l / 2)], r]
        if type(r) == int:
            if r >= 10:
                return [l, [math.floor(r / 2), math.ceil(r / 2)]]
            return None
        res = split(r)
        if res is not None:
            return [l, res]
        return None

    res = split(l)
    if res is not None:
        return [res, r]

    if type(r) == int:
        if r >= 10:
            return [l, [math.floor(r / 2), math.ceil(r / 2)]]
        return None

    res = split(r)
    if res is not None:
        return [l, res]
    return None


def reduce(n):
    new_n = explode(n)
    if new_n is not None:
        return reduce(new_n)
    new_n = split(n)
    if new_n is not None:
        return reduce(new_n)
    return n


def add(l, r):
    return reduce([l, r])


def magnitude(total):
    if type(total) == int:
        return total
    if len(total) == 1:
        return total[0]
    return 3 * magnitude(total[0]) + 2 * magnitude(total[1])


numbers = [eval(line.strip()) for line in open("input.txt")]
total = numbers[0]
for num in numbers[1:]:
    total = add(total, num)


print(magnitude(total))
