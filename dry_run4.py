n = int(input("num"))
low = 1
high = n+1
c = 1
while c<=10:
    m = (low + high)//2
    c=c+1
    if m*m>n:
        high = m
    elif m*m==n:
        print(m)
        break
    else:
        low = m   
else:
    print(m)
# DRY RUN QUESTIONS