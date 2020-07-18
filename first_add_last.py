T = int(input())
for i in range(T):
    user = int(input())
    d = user%10
    user = str(user)
    a = user[0]
    print(d+int(a))