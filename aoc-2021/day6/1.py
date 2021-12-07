fish = [int(i) for i in input().split(",")]

for day in range(80):
    new_fish = []
    for i, f in enumerate(fish):
        if f == 0:
            fish[i] = 6
            new_fish.append(8)
        else:
            fish[i] -= 1
    fish += new_fish

print(len(fish))
