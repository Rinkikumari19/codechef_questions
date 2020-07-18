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

a = int(input("number"))
b = int(input("enter your number"))
c = int(input("number"))
if a+b>c and b+c>a and c+a>b:
    if a==b and b==c and a==c:
        print("equilatale")    
    elif a==c or b==c or a==b:              
        print("isosceles")
    else:
        print("scalene")
else:
    print("invalid traingle")

# It will chexk both things valid triangle and equilatale, isoscelene and scalene



       