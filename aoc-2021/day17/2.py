tx1 = 281
tx2 = 311
ty1 = -74
ty2 = -54


def fire(v):
    positions = [(0, 0), v]
    pos = v
    x, y = pos
    while x <= tx2 and y >= ty1:
        x, y = pos
        vx, vy = v
        new_vx = 0
        if vx > 0:
            new_vx = vx - 1
        if vx < 0:
            new_vx = vx + 1
        v = (new_vx, vy - 1)
        pos = (x + new_vx, y + vy - 1)
        positions.append(pos)
    return positions


def solve():
    count = 0
    for y in range(ty1, 1000):
        for x in range(1000):
            positions = fire((x, y))
            if any(tx1 <= x <= tx2 and ty1 <= y <= ty2 for x, y in positions):
                count += 1

    return count


print(solve())
