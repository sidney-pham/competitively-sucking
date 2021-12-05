from collections import Counter
nums = [line.strip() for line in open('input.txt')]

r1 = nums[:]
r2 = nums[:]

for i in range(len(nums[0])):
    c = Counter([x[i] for x in r1]).most_common()
    if c[0][1] == c[1][1]:
        t = '1'
    else:
        t = c[0][0]
    r1 = list(filter(lambda x: x[i] == t, r1))

    if len(r1) == 1:
        oxygen = r1[0]
        break

for i in range(len(nums[0])):
    c = Counter([x[i] for x in r2]).most_common()
    if c[0][1] == c[1][1]:
        t = '0'
    else:
        t = c[1][0]
    r2 = list(filter(lambda x: x[i] == t, r2))

    if len(r2) == 1:
        scrubber = r2[0]
        break

print(int(oxygen, 2) * int(scrubber, 2))
