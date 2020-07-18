
T = int(input("number"))
r =0
while r<T:
    n = int(input("any number"))
    if n==1:
        print("NO")
    else:
        i = 2
        sum = 0
        while i*i<=n:
            if n%i==0:
                if i==n/i:
                    sum = sum + i
                sum=sum+i+n/i
            i=i+1
        if n==sum+1:
            print("YES")
        else:
            print("NO")
    r=r+1
# PERFECT NUMBER