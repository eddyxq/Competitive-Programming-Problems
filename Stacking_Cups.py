num_cups = int(input())

list = []

for i in range(num_cups):
    a, b = [str(i) for i in input().split()]

    if a.isalpha():
        num = [int(b),a]
    else:
        num = [int(a)/2, b]
    
    list.append(num)

list.sort()
    
for x in range(len(list)):
    print(list[x][1])
    





    
    




