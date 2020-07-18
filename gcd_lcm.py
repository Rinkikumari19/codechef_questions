(a,b) = map(int, input().split())
r = 0
if a<b:
    r = a
else:
    r = b
sum = 1
sum1 = 1
c = 1
while r>=c:
    if a%c==0 and b%c==0:
        sum1=sum1*c
        sum = (sum * c)   
        a = a//c
        b=b//c
    c=c+1
sum = (sum*a*b)
print(sum1,sum)
# GCD AND LCM