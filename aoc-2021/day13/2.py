from itertools import zip_longest

dots = []
folds = []
for line in open("input.txt"):
    if "," in line:
        x, y = map(int, line.strip().split(","))
        dots.append((y, x))
    elif line.startswith("fold"):
        direction, at = line.split(" ")[-1].split("=")
        folds.append((direction, int(at)))

MAX_Y = max(map(lambda x: x[0], dots)) + 1
MAX_X = max(map(lambda x: x[1], dots)) + 1

grid = [["."] * MAX_X for _ in range(MAX_Y)]
for y, x in dots:
    grid[y][x] = "#"

for direction, at in folds:
    print(direction, at)
    if direction == "x":
        left_half = [row[:at] for row in grid]
        right_half = [row[at + 1 :] for row in grid]

        out = []
        for lr, rr in zip(left_half, right_half):
            row = []
            for lc, rc in zip_longest(reversed(lr), rr):
                if lc == "#" or rc == "#":
                    row.append("#")
                else:
                    row.append(".")
            out.append(list(reversed(row)))
    else:
        top_half = grid[:at]
        bottom_half = grid[at + 1 :]

        out = []
        for lr, rr in zip_longest(reversed(top_half), bottom_half):
            row = []
            for lc, rc in zip(lr, rr):
                if lc == "#" or rc == "#":
                    row.append("#")
                else:
                    row.append(".")
            out.append(row)
        out = list(reversed(out))

    grid = out

for row in grid:
    print("".join(row))
