def power(base, exponent):
    total = 1
    for _ in range(exponent):
        total = total * base
    return total

n = int(input())
x = 0
for _ in range(n):
    num = input()
    exponent = int(num[-1])
    base = int(num[:-1])
    x += power(base, exponent)

print(x)