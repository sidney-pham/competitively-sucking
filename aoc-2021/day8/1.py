letters = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def solve(_, output):
    return sum(list(map(len, output)).count(letters[i]) for i in [1, 4, 7, 8])


total = 0
for line in open("input.txt"):
    patterns, output = map(lambda s: s.strip().split(), line.strip().split("|"))
    total += solve(patterns, output)

print(total)
