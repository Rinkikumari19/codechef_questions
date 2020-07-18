
user = int(input("number"))
a = 2
c=0
while a <= user*user:
    b = 2
    while b < a:
        if a%b == 0:
            break
        b=b+1
    else:
        print(a)
        c=c+1
        if c==user:
            break
    a=a+1
# It will print user time prime number




num=int(input("enter any number"))
a=2
count=0
while a<=a*a:
    b=2
    while b<a:
        if a%b==0:
            break
        b=b+1
    else:
        print("prime",a)
        count=count+1
        if count==num:
            break
    a=a+1
