number_of_tests = int(input())

for x in range(number_of_tests):
    r, e, c = [int(i) for i in input().split()]
    if (e - r - c) > 0:
        print("advertise")
    elif (e - r - c) < 0:
        print("do not advertise")
    else:
        print("does not matter")
              
