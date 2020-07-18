
s1 = "aeiouAEIOU"
s2 = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
user = input("enter your number ")
i=0
vowel=0
cons = 0
while i<len(user):
    index=0
    while index<len(s1):
        if user[i]==s1[index]:
            vowel=vowel+1
        else:
            print("",end = "")
        index=index+1
    b=0
    while b<len(s2):
        if user[i]==s2[b]:
            cons=cons+1
        else:
            print("",end = "")
        b=b+1
    i=i+1
print(vowel)
print(cons)

# It is counting vowels and costnant