T = int(input())
for i in range(T):
    N = int(input())
    a = 1
    count = 0
    while a*a <= N:
        count = count+1
        a=a+1
    print(count)
