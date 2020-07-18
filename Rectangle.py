T = int(input())
for i in range(T):
    a,b,c,d = map(int, input().split())
    # print(type(a))
    if a==b==c==d:
        print("YES")
    elif a==b and c==d:
        print("YES")
    elif a==c and b==d:
        print("YES")
    elif a==d and c==b:
        print("YES")
    else:
        print("NO")
