n = int(input())
print(sum(1 if sum(map(int, input().split())) >= 2 else 0 for _ in range(n)))

