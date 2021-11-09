s = input()
if sum(c.isupper() for c in s) > sum(c.islower() for c in s):
    print(s.upper())
else:
    print(s.lower())