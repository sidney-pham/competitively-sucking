n, h = map(int, input().split())
heights = list(map(int, input().split()))

print(sum(1 if height <= h else 2 for height in heights))