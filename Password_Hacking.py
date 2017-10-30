n = int(input())

problist = []

for x in range(0,n):

    list = [str(n) for n in input().split()]

    problist.append(list[1])

problist.sort()
problist.reverse()


guess = 0

for i in range(1,n+1):
    guesses = i * float(problist[i-1])
    guess += guesses

print(guess)
    

    





