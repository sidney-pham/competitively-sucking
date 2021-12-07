from collections import Counter

fish = [int(i) for i in input().split(",")]

timers = Counter(fish)

for day in range(256):
    old_zero = timers[0]
    for i in range(8):
        timers[i] = timers[i + 1]
    timers[8] = old_zero
    timers[6] += old_zero

print(sum(timers.values()))
