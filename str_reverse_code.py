
num = int(input("any number"))
if num<0:
    num=-(num)
num=num
while num>0:
    d=num%10
    print(d,end="")
    num =num//10
print("")