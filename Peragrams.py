from collections import Counter

s = input() # don't call your own variable 'str'

c = Counter(s)

odds = [None for n in c.values() if n % 2]

if odds:
    print(len(odds) - 1)
else:
    print(0)
