T = int(input())
for index in range(T):
    a = 0
    N = int(input())
    while N > 0:
        d = N%10
        a = a*10+d
        N = N//10
    print(a)