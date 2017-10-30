n = int(input())

list = [int(n) for n in input().split()]

total = 0

for n in range(0,n):
    if list[n]<0:
        total+=1

print(total)


