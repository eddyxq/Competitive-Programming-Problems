n = 1

list = [int(n) for n in input().split()]

correctList = [1, 1, 2, 2, 2, 8]

answer = ""


for x in range(len(list)):
    if list[x] > correctList[x]:
        adjustmentNum = correctList[x] - list[x]    
        answer = answer+str(adjustmentNum)+" "
    elif list[x] < correctList[x]:
        adjustmentNum = correctList[x] - list[x]         
        answer = answer+str(adjustmentNum)+" "
    else:
        answer = answer+"0"+" "

print(answer)

