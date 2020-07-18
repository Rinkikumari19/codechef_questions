T = int(input())
for i in range(T):
    K,D0,D1 = map(int, input().split())
    a1 = str(D0)+str(D1)
    d2 = (D0+D1)%10
    a1 = a1+str(d2)
    a1 = int(a1)
    a2 = a1
    
    sum = 0
    while a1 > 0:
        d = a1%10
        sum = sum + d
        a1=a1//10
    sum = (sum%10)
    a2 = str(a2)

    if K > 4:
        k1 = K // 4
        left = K - (k1*4)
        for x in range(k1):
            if sum == 2:
                a2 = a2+str(2486)
            elif sum == 4:
                a2 = a2+str(4862)
            elif sum == 8:
                a2 = a2+str(8624)
            else:
                a2 = a2+str(6248)
        # print(a2)
        print(left)
        if left == 1:
            l2 = int(a2)//1000
            l2 = l2 % 10
            a2 = a2 + str(l2)
        elif left == 2:
            l2 = int(a2)//100
            l2 = l2 % 100
            a2 = a2 + str(l2)
        elif left == 3:
            l2 = int(a2)//10
            l2 = l2%1000
            a2 = a2 + str(l2)
        else:
            a2 = a2
        # print(a2)
        a2 = int(a2)//1000
        print(a2)
    elif K == 3:
        print(a2)
    else:
        print(str(D0) + str(D1))
    print(a2)








# T=int(input())
# for i in range(T) :
#     k,d0,d1 = map(int, input().split())
#     s=d0+d1
#     if s!=10 and k>2 :
#         temp=s%10
#         s=s+temp
#     if s!=10 and s!=20 :
#         s=s + 20*((k-3)//4)
#     x=(k-3)%4
#     for j in range(x) :
#         temp2=s%10
#         s+=temp2
#     if s%3 ==0 :
# 	    print('YES')
#     else :
# 	    print('NO')





