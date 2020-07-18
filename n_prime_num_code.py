a = 2
count = 0
N = int(input())
while True:
    b = 2
    while  a > b:
        if a%b == 0:
            break
        b=b+1
    else:
        print(a)
        count = count+1
        if count == N:
            break
    a=a+1



# user = int(input("number"))
# c = 0
# num = 2
# while c<user:
#     a = 2
#     while a*a<=num:
#         if num%a == 0:
#             break
#         a=a+1
#     else:    
#         print(num)
#         c=c+1
#     num = num + 1
# N PRIME NUMBER