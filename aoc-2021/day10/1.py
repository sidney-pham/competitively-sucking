lines = [line.strip() for line in open("input.txt")]
matching = {
    "]": "[",
    ")": "(",
    "}": "{",
    ">": "<",
}

illegal = []
for line in lines:
    stack = []
    for c in line:
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        else:
            if stack.pop() != matching[c]:
                illegal.append(c)
                break


scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

print(sum(map(scores.get, illegal)))
