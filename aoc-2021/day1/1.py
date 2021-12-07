from itertools import tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


numbers = [int(line.strip()) for line in open("input")]
print(sum(1 for cur, next in pairwise(numbers) if next > cur))
