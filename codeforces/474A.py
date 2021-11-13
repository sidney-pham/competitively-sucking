d = input()
s = input()
keys = "qwertyuiopasdfghjkl;zxcvbnm,./"

print(''.join(keys[keys.index(c) + (1 if d == 'L' else -1)] for c in s))