def parse(line):
    dir, dist = line.split()
    return (dir, int(dist))


commands = [parse(line.strip()) for line in open("input")]


position = 0
depth = 0
for dir, dist in commands:
    if dir == "forward":
        position += dist
    elif dir == "down":
        depth += dist
    else:
        depth -= dist


print(position * depth)
