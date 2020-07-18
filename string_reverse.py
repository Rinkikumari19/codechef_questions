user = int(input("enter your number"))
res=0
if user<0:
    user = user*(-1)
    while user>0:
        a=user%10
        res=res*10+a 
        user = user // 10
    print(res)
else:
    while user>0:
        a=user%10
        res=res*10+a 
        user = user // 10
    print(res)

# It will print reverse order



