
N = int(input())
A = input()
p = A.split()
a=0
# print(p)
while a<len(p):
    b = 0
    while b<len(p)-1:
        if p[b] > p[b+1]:
            p[b],p[b+1] = p[b+1],p[b]
        else:
            p[b],p[b+1] = p[b],p[b+1]
        b=b+1
    a=a+1
print(p)
c = 0
while c<len(p):
    print(p[c])
    c=c+1
# sorting











number =[ 6, 8, -56, 2, 63,-34]
N = int(input())
number = input("any list")
p = number.split()
print(p)
n=0
while n<len(p):   
    i=0
    while i<len(p)-1:
        p[i] = int(p[i])
        if p[i] > int(p[i+1]):
            p[i],p[i+1]=p[i+1],p[i]
        else:
            p[i],p[i+1]=p[i],p[i+1]
        i=i+1
    n=n+1
print(p)
a = 0
while a<len(p):
    print(p[a])
    a=a+1

# OR

# number = input("any list")
# # print()
# p.sort()
# print(p)
# a=0
# while a<len(p):
#     print(p[a])
#     a=a+1

# N = int(input())
# l = []
# for i in range(N):
#     user = int(input())
#     l.append(user)
# l.sort()
# for a in range(len(l)):
#     print(l[a])
# SORT