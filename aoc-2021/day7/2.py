import functools

positions = [int(x) for x in input().split(",")]


@functools.cache
def cost(n):
    return n * (n + 1) // 2


print(
    min(
        sum(cost(abs(pos - to)) for pos in positions)
        for to in range(min(positions), max(positions) + 1)
    )
)
