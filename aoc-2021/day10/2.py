lines = [line.strip() for line in open("input.txt")]
matching = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">",
}
matching_inv = {
    "]": "[",
    ")": "(",
    "}": "{",
    ">": "<",
}

legal = []
for line in lines:
    stack = []
    for c in line:
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        else:
            if stack.pop() != matching_inv[c]:
                break
    else:
        legal.append(line)
        print("remaining", stack)

print(legal)

completions = []
for line in legal:
    stack = []
    for c in line:
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        else:
            d = stack.pop()
            # print(c, d)
            if matching[d] != c:
                print(c, d)
    completions.append(list(map(matching.get, list(reversed(stack)))))

# for c in completions:
#     print("".join(c))

scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

all_scores = []
for completion in completions:
    total = 0
    for c in completion:
        total *= 5
        total += scores[c]
    all_scores.append(total)

print(all_scores)

i = len(all_scores) // 2
# print(i)
print(sorted(all_scores)[i])
# [len(all_scores) // 2 + 1])
