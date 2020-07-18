n = int(input("num"))
res = 1
p = 2
while p<=n:
    c=0
    while n%p==0:
        c=c+1
        n=n//p
    else:
        res=res*(c+1)
        p=p+1
else:
    print(res)

# this is also dry run
















