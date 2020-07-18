num = int(input())
a = 2
while a*a<=num:
    if num%a == 0:
        print("not prime")
        break
    a=a+1
else:    
    print(num,'prime')   
