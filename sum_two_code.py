T = int(input())
for i in range(T):
    (A,B) = map(int, input().split())
    if A>B:
        c = A
    else:
        c = B
    print(c,(A+B))