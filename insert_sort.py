# number = [-2,45,0,-8,11,-9,2]
# n=0
# while n<len(number):
#     i=0
#     while i<len(number)-1:
#         if number[i] > number[i+1]:
#             number[i],number[i+1]=number[i+1],number[i]
#         else:
#             number[i],number[i+1]=number[i],number[i+1]
#         i=i+1
#     n=n+1
# print(number)
 



T = int(input())
l = []
user = int(input())
l.append(user)
a = 0
while a < (T-1):
    user1 = int(input())
    l.append(user1)
    b = -1
    while b >= -(len(l)-1):
        if l[b] >= l[b-1]:
            l[b],l[b-1]=l[b],l[b-1]
        else:
            l[b],l[b-1]=l[b-1],l[b]
        b=b-1
    a=a+1
# print(l)
for x in range(len(l)):
    print(l[x])
        