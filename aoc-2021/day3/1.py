from collections import Counter
nums = [line.strip() for line in open('input.txt')]

gamma = []
epsilon = []

for i in range(len(nums[0])):
    c = Counter([x[i] for x in nums]).most_common()
    gamma.append(c[0][0])
    epsilon.append(c[1][0])

gamma = ''.join(gamma)
epsilon = ''.join(epsilon)


print(int(gamma, 2) * int(epsilon, 2))