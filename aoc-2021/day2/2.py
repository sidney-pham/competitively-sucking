def parse(line):
    dir, dist = line.split()
    return (dir, int(dist))


commands = [parse(line.strip()) for line in open("input")]

position = 0
depth = 0
aim = 0
for dir, dist in commands:
    if dir == "down":
        aim += dist
    elif dir == "up":
        aim -= dist
    else:
        position += dist
        depth += aim * dist

print(position * depth)
