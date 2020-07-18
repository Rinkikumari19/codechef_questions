num=int(input("enter your number"))
a=1
while a<=num:
    b=1
    while b<=a:
        if a*b==num:
            print(b,a)   
        b=b+1
    a=a+1

# It is printing HCF of num


