
# num = int(input("enter your number"))
# if num%5==0:
#     print("divisible hai")
# else:
#     print("divisible nahi hai")

# If num will divisible by 5 so it will print divisible hai

N = int(input("any num"))
i = 0
while i<N:
    l = input("num")
    a = l.split()
    r = int(a[0]) % int(a[1])
    print(r)
    i=i+1



# N = int(input())
# i = 0
# while i<N:
#     (a, b, c) = map(int, input().split())
#     if a>b and a<c:
#         print(a)
#     elif a<b and a>c:
#         print(a)
#     elif b>a and b<c:
#         print(b)
#     elif b<a and b>c:
#         print(b)
#     else:
#         print(c)
    # i=i+1

# user = int(input("enter your number"))
# if user%3==0 and user%2!=0:
#     print("odd")
# else:
#     print("not odd")

# If it will divisble by 3 and odd also so it will print odd
 

# user = int(input("number"))
# c = 0
# num = 2
# while c<user:
#     a = 2
#     while a*a<=num:
#         while num%a ==0:
#             num = num +1
#         a=a+1
#     print(num)
#     num = num + 1
#     c=c+1
# prime number

# T = int(input())
# for tc in range(T):
# 	# Read integers a and b.
# 	(a, b) = map(int, input().split(' '))
# print(a+b)


# N = int(input())
# a = 0
# while a<N:
#     x,y,z = int(input()).split()
#     if x>y and x>z:
#         print(x)
#     elif y>x and y>z:
#         print(y)
#     else:
#         print(z)
#     a=a+1




# T = int(input())
# a=1
# b = 10
# while a<=T:
#     num = int(input())
#     print(num*b)
#     a=a+1
#     b=b*10
    



# number = int(input("enter your number"))
# if number%11==0 and number%5==0:
#     print("both")
# elif number%5==0:
#     print(5)
# elif number%11==0:
#     print(11)
# else:
#     print("none")

# It will check by 11 and 5 both then acording to condition it will print




# sp = int(input("enter your number"))
# cp = int(input("enter your number"))
# if sp>cp:
#     print("profit")
# elif sp<cp:
#     print("loss")
# else:
#     print("no profit, no loss")

# It will check profit or loss





# a = int(input("enter your num"))
# b = int(input("enter your number"))
# c = int(input("enter your num"))
# if a+b>c and a+c>b and b+c>a:
#     print("valid triangle")
# else:
#     print("invalid triangle")


# If two side greter than third side so it will valid tringle




# a=int(input("enter num"))
# b = int(input("num"))
# c = int(input("number"))
# if a==b and b==c:
#     print("equilatered")
# elif a==c or b==c or a==b:
#     print("isosceles")
# else:
#     print("scalene")

# It will check that triangle is equilatered(barabar), isosceles(two sides equale) or scalene(all sides are different)





# a=int(input("number"))
# b=int(input("any num"))
# c=int(input("any num"))
# if a+b>c:
#     if a+c>b:
#         if b+c>a:
#             if a==b==c:
#                 print("equilateral")
#             elif a==b!=c:
#                 print("isosceles")
#             elif a==c!=b:
#                 print("isosceles")
#             elif b==c!=a:
#                 print("isosceles")
#             else:
#                 print("sceles")
#         else:
#             print("invalid")
#     else:
#         print("invalid")
# else:
#     print("invalid")

        # OR

# a = int(input("number"))
# b = int(input("enter your number"))
# c = int(input("number"))
# if a+b>c and b+c>a and c+a>b:
#     if a==b and b==c and a==c:
#         print("equilatale")    
#     elif a==c or b==c or a==b:              
#         print("isosceles")
#     else:
#         print("scalene")
# else:
#     print("invalid traingle")

# It will chexk both things valid triangle and equilatale, isoscelene and scalene



       

# s1 = int(input("enter your number"))
# s2 = int(input("enter your number"))
# s3 = int(input("enter your number"))
# r = s1 + s2
# if r+s3==180:
#     print("possible tringle")
# else:
#     print("not possible tringle")

# It will check that it's sum of three sides equal to 180' so it will possible triangle




# s1 = int(input("enter your number"))
# s2 = int(input("number"))
# s3 = int(input("number"))
# if s1==90 or s2==90 or s3==90:
#     print("right angle")
# elif s1>90 or s2 > 90 or s3 > 90 :
#     print("obtuse")
# else:
#     print("acute")

# It will check that which type triangle is there like right angle, obtuse angle or acute angle.



# s1 = int(input("enter your number"))
# s2 = int(input("number"))
# s3 = int(input("number"))
# p = s1 + s2
# if p+s3==180:
#     if s1==90 or s2==90 or s3 ==90:
#         print("right angle")
#     elif s1>90 or s2>90 or  s3>90:
#         print("obtuse")
#     else:
#         print("acute")
# else:
#     print("invalid triangle")

# It will check both things, triangle is valid or not and which type triangle are there, this thing also.




# a=0
# b=1
# n = int(input("enter your number"))
# if n==1:
#     print(a)
# elif n==2:
#     print(a,b)
# else:
#     print(a,b)
#     i=1
#     while i<=n-2:
#         c=a+b
#         a=b
#         b=c
#         i=i+1
#         print(c)

#         this is dry run question




# num = int(input("enter your number"))
# sum=0
# a=1
# while a<=num:
#     user = int(input("num"))
#     sum=sum+user
#     a=a+1
# print(sum)

# It will print sum of num which taken by input





# num = int(input("enter your number"))
# a=1
# while a<=num:
#     user = int(input("num"))
#     if user%2==0:
#         print("even")
#     else:
#         print("odd")
#     a=a+1


# It will take input from num and it will check it is odd or even



# user = int(input("enter your number"))
# a=1
# sum = 0
# while a<=user:
#     sum = sum+a
#     a=a+1
# print(sum)

# print sum of user



# user = int(input("number"))
# a=0
# while user>a:
#     print(user)
#     user = user-1

# It will print reverse order of user




# n = int(input("num"))
# low = 1
# high = n+1
# c = 1
# while c<=10:
#     m = (low + high)//2
#     c=c+1
#     if m*m>n:
#         high = m
#     elif m*m==n:
#         print(m)
#         break
#     else:
#         low = m   
# else:
#     print(m)

# # dry run question


# n = int(input("num"))
# res = 1
# p = 2
# while p<=n:
#     c=0
#     while n%p==0:
#         c=c+1
#         n=n//p
#     else:
#         res=res*(c+1)
#         p=p+1
# else:
#     print(res)

# this is also dry run





# b = 1
# a=int(input("number"))
# c= "*"
# d = "="
# while b<=10:
#     print(a,c,b,d,(a*b))
#     b=b+1

# It will print table of any number




# a=1
# b=1
# while a<11:
#     b=b*a
#     a=a+1
# print(b)

# It will print 1*2*3*4...10



# a=3
# count=0
# while a<=14*14:
#     if a%2==1:
#         count = count+1
#         print(a)
#         if count==14:
#             break
#     a=a+1

# It will print starting 14 odd number




# a=1
# name = input("any name")
# while a<=20:
#     print("Hello",name)
#     a=a+1

# It will print twenty times hello and which name I will give in input



# num = int(input("enter your number"))
# sum = 0
# if num<0:
#     num=-(num)
# num=num
# while num>0:
#     d=num%10
#     sum=sum+d
#     num=num//10
# print(sum)


# It will print sum of digits 



# num = int(input("any number"))
# if num<0:
#     num=-(num)
# num=num
# while num>0:
#     d=num%10
#     print(d,end="")
#     num =num//10
# print("")





# num = int(input("enter your number"))
# if num<0:
#     num=-(num)
# num = num
# while num>0:
#     a=num%100
#     if a//10==7:
#         print("yes")
#     else:
#         print("no")
#     break
# second elements it should 7




# user=int(input("any num"))
# a=1
# sum=0
# while a<user:
#     if user%a==0:
#         sum=sum+a
#     a=a+1
# if sum==user:
#     print("perfect number")
# else:
#     print("not perfect number")

# It will print perfect number like 6=1+2+3




# user=int(input("enter any num"))
# a=1
# count=0
# while a<=user:
#     if user%a==0:
#         count=count+1
#     a=a+1
# if count==2:
#     print("prime number")
# else:
#     print("not prime number")

# It will print prime number, user is prime number or not







# num=int(input("enter any number"))
# a=2
# count=0
# while a<=a*a:
#     b=2
#     while b<a:
#         if a%b==0:
#             break
#         b=b+1
#     else:
#         print("prime",a)
#         count=count+1
#         if count==num:
#             break
#     a=a+1

# The more we give the number to the user, the more the prime number will print
    



# user1 = int(input("enter your number"))
# user2 = int(input("enter your number"))
# a=1
# if user1>user2:
#     r = user2
# else:
#     r = user1
# while a<=r:
#     if user1%a==0:
#         if user2%a==0:
#             d=a
#     a=a+1
# print(d)


# It will print highest common factor after nultiply two numbers(HCF)





# num=int(input("enter your number"))
# a=1
# while a<=num:
#     b=1
#     while b<=a:
#         if a*b==num:
#             print(b,a)   
#         b=b+1
#     a=a+1

# It is printing HCF of num





# num=int(input("num"))
# if num%10==7:
#     print("yes")
# else:
#     print("nahi")
# If last element will 7 so it will print yes



# a=65475
# b=a%100
# print(b//10)
# ye number ka last second digit print krega 7

        # OR

# num=int(input("enter any number"))
# b=num%100
# if b//10==7:
#     print("yes")
# else:
#     print("nahi")
# It is checking last second element is 7 or not




# user = int(input("enter your number"))
# a=1
# while a*a<=user:
#     if user%a==0:
#         print(a,user//a)
#     a=a+1

# it is factor printing





# user = str(input("enter your num"))
# sum = 0
# i=0
# while i < len(user):
#     sum = sum + int(user[i])
#     i=i+1
# print (sum)
# Is is printing sum of string number 




# a = int(input("num"))
# s=0 
# if a<0:
#     a=-(a)
# if a==0:
#     print(a)
# else:
#     while a>0:
#         d=a%10
#         print(d)
#         s=s+d
#         a=a//10
#     print(s)

# It will print sum of reverse number negetive also




# num=1
# while num<1000: 
#     a=num
#     sum=0
#     while a>0:
#         b=a%10
#         c=b*b*b
#         sum=sum+c
#         a=a//10
#     if sum==num:
#         print("armsrong number",num)
#     num=num+1

# It is printing armstrong number between 1 to 1000




# user = int(input("enter your number"))
# res=0
# if user<0:
#     user = user*(-1)
#     while user>0:
#         a=user%10
#         res=res*10+a 
#         user = user // 10
#     print(res)
# else:
#     while user>0:
#         a=user%10
#         res=res*10+a 
#         user = user // 10
#     print(res)

# It will print reverse order




# user=int(input("enter your number"))
# r=user
# sum=0
# while user>0:
#     a=user%10
#     c=1
#     b=1
#     while a>=c:
#         b=b*c
#         c=c+1
#     sum=sum+b    
#     user=user//10
# if user<0:
#     user = user*(-1)
#     while user>0:
#         a=user%10
#         c=1
#         b=1
#         while a>=c:
#             b=b*c
#             c=c+1
#         sum=sum+b   
#     user=user//10
# if sum==r:
#     print("strong number hai")
# else:
#     print("strong number nahi hai") 

# user=int(input("enter your number"))
# sum=0
# if user < 0:
#     user = -user
# user = user
# r=user
# while user>0:
#     a=user%10
#     c=1
#     b=1
#     while a>=c:
#         b=b*c
#         c=c+1
#     sum=sum+b    
#     user=user//10
# if sum==r:
#     print("strong number hai")
# else:
#     print("strong number nahi hai") 



# It will check that this is strong number or not 



# a=1
# while a<=5:
#     b=1
#     while b<=5:
#         print(b,end=" ")
#         b=b+1
#     print("\n")
    # new line print krega
    # a=a+1

# It will print pattern 12345




# r=0
# a=626
# c=a
# while a>0:
#     b = a%10
#     r=r*10+b
#     a=a/10
# if r==c:
#     print("palindrom hai")
# else:
#     print("palindrom nhi hai")

# It is cheking a is palindrom or not like start and end side both are looking same



# a=1
# while a<=6:
#     b=1
#     while b<a:
#         print(b)
#         b=b+1
#     c=b-1
#     while c>1:
#         c=c-1
#         print(c) 
#     print("\n")
#     a=a+1

# It will print pattern








# num =int(input("number"))
# a=1
# while a<=num:
#     j=num-1
#     while j>=a:
#         print(" ",end="")
#         j=j-1
#     k=1
#     while k<=a:
#         print("*",end="")
#         k=k+1
#     print("\n")
#     a=a+1

# It will print opposite star





# user = int(input("number"))
# a = 2
# c=0
# while a <= user*user:
#     b = 2
#     while b < a:
#         if a%b == 0:
#             break
#         b=b+1
#     else:
#         print(a)
#         c=c+1
#         if c==user:
#             break
#     a=a+1
# It will print user time prime number

 



# a=1
# b=[]
# while a<=5:
#     user = input("name ")
#     b.append(user)
#     a=a+1
# c=-1
# while -len(b)<=c:
#     print(b[c])
#     c=c-1 
#     reverse name print krega




# l = ["a",1, "2", 5, "b", "q"]
# user = int(input("enter your number"))
# i=0
# count = 0
# while i<user:
#     a=-1
#     r =[]
#     while -user<=a:
#         r.append(l[a])
#         count = count+1
#         if count == user:
#             x=-1
#             while x>=-len(r):
#                 print(r[x])
    #             x=x-1
    #     a=a-1
    # i=i+1

# It will print last number od user
   
 
    


# num = [1,2,3,4,5,6,7]
# user = int(input("number"))
# i=0
# while i<len(num):
#     if user == num[i]:
#         print("yes")
#         break
#     i=i+1
# else:
#     print("nahi")

# It will chacke user's number in num or not

# a=1
# list = []
# while a<=25:
#     user = input("name ")
#     list.append(user)
#     a=a+1
# c = -1
# while -len(list) <= c:
#     print(list[c])
#     c=c-1
# LIST IN REVERSE



# a = 1
# while a<=5:
#     b=1
#     while b<=5:
#         print(b,end="")
#         b=b+1
#     print("\n")
#     a=a+1
    # PATTERN



# a=1
# while a<=10:
#     num = int(input("enter your number"))
#     if num%2==0:
#         print(num*100)
#     else:
#         print(num*(-1))
#     a=a+1      

# If num will even so it will multiply by 100 and odd so multiply by -1   





# a=2
# x=3
# print(1)
# while a<6:
#     b=a
#     while b<=x:
#         print(b,end="")
#         b=b+1
#     c=b-2
#     while c>=a:
#         print(c,end="")
#         c=c-1       
#     print("\n")
#     a=a+1
#     x=x+2

# It will print pattern

   


# i=0
# l = []
# while i<7:
#     user = int(input("enter your number"))
#     l.append(user)
#     i=i+1
# print(l)
# x=0
# b=1
# while x<len(l)-1:
#     if l[x]==l[b]-1:
#         print("its consective number")
#         x=x+1
#         b=b+1
#     else:
#         print("not consecutive number")
#         break
# It's cheking distance 1 in every elements





# s1 = "aeiouAEIOU"
# s2 = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
# user = input("enter your number ")
# i=0
# vowel=0
# cons = 0
# while i<len(user):
#     index=0
#     while index<len(s1):
#         if user[i]==s1[index]:
#             vowel=vowel+1
#         else:
#             print("",end = "")
#         index=index+1
#     b=0
#     while b<len(s2):
#         if user[i]==s2[b]:
#             cons=cons+1
#         else:
#             print("",end = "")
#         b=b+1
#     i=i+1
# print(vowel)
# print(cons)

# It is counting vowels and costnant




# a=1
# while a<26:
#     if a%5==0:
#         print(a)
#     else:
#         print(a,(" "), end="")
#     a=a+1 
# assending 5 count pattern printing



    


# l = []
# i=0
# while i<10:
#     user = int(input("enter your number"))
#     l.append(user)
#     i=i+1
# p = l[1]-l[0]
# a=0
# while a<len(l)-1:
#     if l[a]==l[a+1]-p:
#         a=a+1
#     else:
#         print("conscetive progress number nhi hai")
#         break
# else:
#     print("consective progressive number hai") 

# distance equale it will check between elements





# i = 5
# b=0
# while i<=25:
#     a = i
#     while a>b:
#         print(a,end="")
#         a=a-1
#     print("\n")
#     b = i
#     i = i + 5

# pattern disanding order of 5




# i=5
# b=0
# while i<=25:
#     a=i
#     if a%2!=0:
#         b=b+1
#         while b<=a:
#             print(b,end="")
#             b=b+1
#     else:
#         while a>b:
#             print(a,end="")
#             a=a-1
#     b=i
#     i=i+5
#     print("\n")

# It will print asending or disanding order pattern of 5

        

# a=-15
# b=-(a)
# print(b)
# while a<=-10: 
#     print(a)
#     b=b-1 
#     a=-(b)
# it will print -15 to -10
   



# num = int(input("number"))
# r = 0
# if num < 0:
#     num = -num
# a=num
# while num>0:
#     b = num % 10
#     r = r * 10 + b
#     num = num//10
# if a==r:
#     print("palindrom")
# else:
#     print("not palindrom") 



# num = 1
# while num < 1000:
#     a = num
#     sum = 0
#     while a > 0:
#         b=a%10
#         c = b*b*b
#         sum = sum +c
#         a=a//10
#     if sum == num:
#         print("armstrong number = ",num)
#     num = num +1




# num = int(input("number"))
# a = 1
# sum = 0
# while num>0:
#     a=num%10
#     sum = sum+a
#     num = num//10
# while num<0:
#     num = num(-1)
#     a=num%10
#     sum = sum+a
#     num = num//10
# else:
#     print(sum)

# user=int(input("enter any num"))
# a=1
# count=0
# while a*a<=user:
#     if user%a==0:
#         count=count+1
#     a=a+1
# if count==2:
#     print("prime number")



