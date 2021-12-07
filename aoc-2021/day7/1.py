positions = [int(x) for x in input().split(",")]

print(
    min(
        sum(abs(pos - to) for pos in positions)
        for to in range(min(positions), max(positions) + 1)
    )
)
