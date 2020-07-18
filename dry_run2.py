a=0
b=1
n = int(input("enter your number"))
if n==1:
    print(a)
elif n==2:
    print(a,b)
else:
    print(a,b)
    i=1
    while i<=n-2:
        c=a+b
        a=b
        b=c
        i=i+1
        print(c)

#         this is dry run question

