n = int(input())

for x in range(n):
    empty = input()
    candies = 0
    numOfKids = int(input())
    for y in range(numOfKids):
        numOfCandies = int(input())
        candies += numOfCandies
    if candies % numOfKids == 0:
        print("YES")
    else:
        print("NO")