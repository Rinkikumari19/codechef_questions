num = [1,2,3,4,5,6,7]
user = int(input("number"))
i=0
while i<len(num):
    if user == num[i]:
        print("yes")
        break
    i=i+1
else:
    print("nahi")