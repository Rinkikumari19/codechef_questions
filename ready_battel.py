N = int(input("num"))
i = 1
l = []
while i <= N:
    A = int(input("number"))
    l.append(A)
    i = i + 1
j = 0
count1 = 0
count2 =0
while j<len(l):
    if l[j]%2==0:
        count1 = count1+1
    else:
        count2 = count2 + 1
    j=j+1
if count1 > count2:
    print("READY FOR BATTLE")
else:
    print("NOT READY")

