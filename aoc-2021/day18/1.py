import math


MARKER = float("inf")


def explode(n):
    exploded = False

    def _explode(n, depth, carry=0):
        l, r = n

        if depth == 4:
            nonlocal exploded
            if not exploded:
                exploded = True
                # n[0] = MARKER
                # n[1] = MARKER
                return [MARKER, MARKER], (l, r)
            return n, (0, 0)
        if type(l) != int:
            l, (dl, dr) = _explode(l, depth + 1, carry=carry)
            if type(r) == int:
                return [l, r + dr], (dl, 0)
            r, (dl, dr) = _explode(r, depth + 1, carry=dr)
            return [l, r], (dl, dr)

        l += carry
        if type(r) != int:
            r, (dl, dr) = _explode(r, depth + 1)
            return [l + dl, r], (0, dr)

        return [l, r], (0, 0)

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
            n[0] = [math.floor(l / 2), math.ceil(l / 2)]
            return n
        if type(r) == int:
            if r >= 10:
                n[1] = [math.floor(r / 2), math.ceil(r / 2)]
                return n
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
            n[1] = [math.floor(r / 2), math.ceil(r / 2)]
            return n
        return None

    res = split(r)
    if res is not None:
        return [l, res]
    return None


def reduce(n):
    # If pair is inside 4 other pairs, leftmost explodes.
    # Elif any regular number is >= 10, the leftmost splits.
    # If no actions were applied, we're done.
    # Otherwise, reduce again.
    new_n = explode(n)
    if new_n is not None:
        return reduce(new_n)
    new_n = split(n)
    if new_n is not None:
        return reduce(new_n)
    return n


def add(l, r):
    return reduce([l, r])


numbers = [eval(line.strip()) for line in open("input2.txt")]
numbers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
# print(numbers)
total = numbers[0]
for num in numbers[:-1]:
    total = add(total, num)
    print(total)
print(total)


# def magnitude(total):
#     if type(total) == int:
#         return total
#     if len(total) == 1:
#         return total[0]
#     return 3 * magnitude(total[0]) + 2 * magnitude(total[1])


# print(magnitude(total))


# Tests
s1 = [[[[[9, 8], 1], 2], 3], 4]
s2 = [7, [6, [5, [4, [3, 2]]]]]
s3 = [[6, [5, [4, [3, 2]]]], 1]
s4 = [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]
s5 = [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]

assert explode(s1) == [[[[0, 9], 2], 3], 4]
assert explode(s2) == [7, [6, [5, [7, 0]]]]
assert explode(s3) == [[6, [5, [7, 0]]], 3]
assert explode(s4) == [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
assert explode(s5) == [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]

assert explode([[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]) == [
    [[[0, 7], 4], [7, [[8, 4], 9]]],
    [1, 1],
]
assert explode([[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]]) == [
    [[[0, 7], 4], [15, [0, 13]]],
    [1, 1],
]
assert split([[[[0, 7], 4], [15, [0, 13]]], [1, 1]]) == [
    [[[0, 7], 4], [[7, 8], [0, 13]]],
    [1, 1],
]
assert split([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]) == [
    [[[0, 7], 4], [[7, 8], [0, [6, 7]]]],
    [1, 1],
]
assert explode([[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]) == [
    [[[0, 7], 4], [[7, 8], [6, 0]]],
    [8, 1],
]
a4 = add(add(add([1, 1], [2, 2]), [3, 3]), [4, 4])
assert a4 == [[[[1, 1], [2, 2]], [3, 3]], [4, 4]]
assert add(a4, [5, 5]) == [[[[3, 0], [5, 3]], [4, 4]], [5, 5]]
assert add(add(a4, [5, 5]), [6, 6]) == [[[[5, 0], [7, 4]], [5, 5]], [6, 6]]

assert add(
    [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
    [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
) == [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]]

print("All tests passed!!!")
