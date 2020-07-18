num=1
while num<1000: 
    a=num
    sum=0
    while a>0:
        b=a%10
        c=b*b*b
        sum=sum+c
        a=a//10
    if sum==num:
        print("armsrong number",num)
    num=num+1

# It is printing armstrong number between 1 to 1000








