import math


a,n = input().split()

a = float(a)
n = float(n)

cir = 2*math.pi*(a/math.pi)**0.5

if n >= cir:
    print("Diablo is happy!")
else:
    print("Need more materials!")
