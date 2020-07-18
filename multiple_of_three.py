T = int(input("enter your test cases "))
for i in range(T):
    k,d0,d1 = map(int, input().split())
    num = d0 + d1
    sum_str = str(d0) + str(d1)
    if k > 2:
        sum_str = sum_str + str(num)
        sum_str = int(sum_str)
        count1 = 0
        sum2_str = sum_str
        while sum_str > 0:
            d = sum_str % 10
            count1 = count1 + 1
            sum_str = sum_str//10
        print(count1)
        print(sum2_str)
        sum3_str = str(sum2_str)
        while k > count1:
            sum = 0
            while sum2_str > 0:
                d1 = sum2_str % 10
                sum = sum + d1
                sum2_str = sum2_str//10
            a = sum%10
            print(sum)
            if sum > 9:
                sum3_str = sum3_str + str(a)
            else:
                sum3_str = sum3_str + str(sum)
                print(sum3_str)
            sum2_str = int(sum3_str)
            count1 = count1 + 1
        else:
            print(sum3_str)
            if int(sum3_str) % 3 == 0:
                print("YES")
            else:
                print("NO")
    else:
        if int(sum_str) % 3 == 0:
            print("YES")
        else:
            print("NO")

   



# a = 243
# sum = 0
# while a>0:
#     b = a%10
#     sum = sum + b
#     a = a //10
# print(sum)
  
    
       
        

# 3
# 5 3 4
# 13 8 1
# 760399384224 5 1
    
  