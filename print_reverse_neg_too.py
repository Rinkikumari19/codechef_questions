a = int(input("num"))
s=0 
if a<0:
    a=-(a)
if a==0:
    print(a)
else:
    while a>0:
        d=a%10
        print(d)
        s=s+d
        a=a//10
    print(s)

# It will print sum of reverse number negetive also


