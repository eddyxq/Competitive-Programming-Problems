list = [i for i in input()]

cup1 = 1
cup2 = 0
cup3 = 0


for x in range(len(list)):
    if list[x] == "A":
        if cup1 == 1:
            cup1 = 0
            cup2 = 1
        elif cup2 == 1:
            cup1 = 1
            cup2 = 0

    elif list[x] == "B":
        if cup2 == 1:
            cup2 = 0
            cup3 = 1
        elif cup3 == 1:
            cup3 = 0
            cup2 = 1

    elif list[x] == "C":
        if cup1 == 1:
            cup1 = 0
            cup3 = 1
        elif cup3 == 1:
            cup3 = 0
            cup1 = 1


if cup1 == 1:
    print("1")
elif cup2 == 1:
    print("2")
else:
    print("3")