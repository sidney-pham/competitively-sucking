from itertools import permutations

# Canonical form:
#  111
# 2   3
# 2   3
# 2   3
#  444
# 5   6
# 5   6
# 5   6
#  777

segments_to_digit = {
    (1, 2, 3, 5, 6, 7): 0,
    (3, 6): 1,
    (1, 3, 4, 5, 7): 2,
    (1, 3, 4, 6, 7): 3,
    (2, 3, 4, 6): 4,
    (1, 2, 4, 6, 7): 5,
    (1, 2, 4, 5, 6, 7): 6,
    (1, 3, 6): 7,
    (1, 2, 3, 4, 5, 6, 7): 8,
    (1, 2, 3, 4, 6, 7): 9,
}

length_to_segments = {
    2: [{3, 6}],
    3: [{1, 3, 6}],
    4: [{2, 3, 4, 6}],
    5: [{1, 3, 4, 5, 7}, {1, 3, 4, 6, 7}, {1, 2, 4, 6, 7}],
    6: [{1, 2, 3, 5, 6, 7}, {1, 2, 4, 5, 6, 7}, {1, 2, 3, 4, 6, 7}],
    7: [{1, 2, 3, 4, 5, 6, 7}],
}


def solve(patterns, output):
    valids = []
    # configuration := assignment of letter to number
    configurations = [dict(zip("abcdefg", p)) for p in permutations(range(1, 8))]
    for configuration in configurations:
        for pattern in patterns:
            if (
                set(map(configuration.get, pattern))
                not in length_to_segments[len(pattern)]
            ):
                break
        else:
            valids.append(configuration)
    valid_configuration = valids[0]

    digits = [
        segments_to_digit[tuple(sorted(map(valid_configuration.get, o)))]
        for o in output
    ]
    return int("".join(map(str, digits)))


total = 0
for line in open("input.txt"):
    patterns, output = map(lambda s: s.strip().split(), line.strip().split("|"))
    total += solve(patterns, output)

print(total)
