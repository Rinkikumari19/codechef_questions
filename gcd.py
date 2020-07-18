T = int(input("any number"))
for i in range(T):
    A,B = map(int, (input().split()))
    if A>B:
        z = B
    else:
        z = A
    gcd = 1
    while 1<=z:
        if A%z==0 and B%z==0:
            gcd=gcd*z
            break   
        z=z-1
    p = A/gcd
    q = B/gcd
    lcm = gcd*p*q
    print(gcd,int(lcm))