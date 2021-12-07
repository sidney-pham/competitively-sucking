# Not swag.
numbers = [int(line.strip()) for line in open("input")]

count = 0
last = float("inf")
for l in range(len(numbers) - 2):
    r = l + 2
    s = sum(numbers[l : r + 1])
    if s > last:
        count += 1
    last = s

print(count)
