x = int(input())
n = int(input())

total = 0
remaining = 0
avaliable = 0

for _ in range(n):
    gb_spent = int(input())
    remaining = x - gb_spent
    avaliable += remaining

print(avaliable+x)