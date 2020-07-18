
a = int(input("any num"))   
n = input("any number")
n = n.split()
r = 0
if n[0]>n[1]:
    r = n[0]
else:
    r = n[1]
print(r)

b = 1
sum = 1
n[0] = int(n[0])
n[1]= int(n[1])
# print(type(n[0]))
r = int(r)
print(type(r))
sum1 = 1
while r>=b:
    if n[0]%b==0 and n[1]%b==0:
        sum1=sum1*b
        sum = (sum * b)
        # print(b)
        n[0] = n[0]/b
        n[1]=n[1]/b
    r=r+1
sum = (sum * n[0]*n[1])
print(sum)
print(sum1)




