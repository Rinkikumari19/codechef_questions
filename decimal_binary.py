

N = int(input("any num"))
s = 0
while s<N:
    n = int(input("any number"))
    b=[]
    while n>0:
    # c=(n%2)
        b.append(n%2)
        n = n/2
        n = int(n)
# print(b)
    a = -1
    while a>=-(len(b)):
        print(b[a],end="")
        a=a-1
    print()
    s=s+1
# DECIMAL TO BINARY CONVERT