

user=int(input("enter your number"))
r=user
sum=0
while user>0:
    a=user%10
    c=1
    b=1
    while a>=c:
        b=b*c
        c=c+1
    sum=sum+b    
    user=user//10
if sum==r:
    print("strong number hai")
else:
    print("strong number nahi hai") 

# It will check that this is strong number or not 