T = int(input())
for i in range(T):
    N = int(input())
    count = 0
    for index in range(1,N+1):
        if N%index==0:
            count = count + 1
    if count == 2:
        print("YES")
    else:
        print("NO")
