from itertools import cycle, islice
n, k = map(int, input().split())

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[:k] + ''.join(islice(cycle('ab'), n - k)))