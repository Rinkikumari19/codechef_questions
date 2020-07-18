s1 = int(input("enter your number"))
s2 = int(input("number"))
s3 = int(input("number"))
p = s1 + s2
if p+s3==180:
    if s1==90 or s2==90 or s3 ==90:
        print("right angle")
    elif s1>90 or s2>90 or  s3>90:
        print("obtuse")
    else:
        print("acute")
else:
    print("invalid triangle")

# It will check both things, triangle is valid or not and which type triangle are there, this thing also.
















