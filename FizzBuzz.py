list = [int(n) for n in input().split()]

x = list[0]
y = list[1]
n = list[2]

for i in range(1, n+1):
    if i % x == 0 and i % y == 0:
        print("FizzBuzz")
    elif i % x == 0 and i % y != 0:
        print("Fizz")
    elif i % x != 0 and i % y == 0:
        print("Buzz")
    else:
        print(i)







