T = int(input())
for i in range(T):
    user = int(input())
    fac = 1
    for j in range(1,user+1):
        fac = fac * j
    print(fac)
