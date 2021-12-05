from collections import defaultdict

floor = defaultdict(lambda: defaultdict(int))

def fill(x1, y1, x2, y2):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            floor[y][x] += 1

def solve(floor):
    count = 0
    for row in floor.values():
        for cell in row.values():
            if cell >= 2:
                count += 1
    return count

for line in open('input.txt'):
    p1, p2 = line.strip().split('->')
    x1, y1 = map(int, p1.split(','))
    x2, y2 = map(int, p2.split(','))
    
    if x1 == x2 or y1 == y2:
        fill(x1, y1, x2, y2)

print(solve(floor))
