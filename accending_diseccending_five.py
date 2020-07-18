 i=5
b=0
while i<=25:
    a=i
    if a%2!=0:
        b=b+1
        while b<=a:
            print(b,end="")
            b=b+1
    else:
        while a>b:
            print(a,end="")
            a=a-1
    b=i
    i=i+5
    print("\n")

# It will print asending or disanding order pattern of 5

        