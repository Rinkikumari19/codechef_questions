l = ["a",1, "2", 5, "b", "q"]
user = int(input("enter your number"))
i=0
count = 0
while i<user:
    a=-1
    r =[]
    while -user<=a:
        r.append(l[a])
        count = count+1
        if count == user:
            x=-1
            while x>=-len(r):
                print(r[x])
                x=x-1
        a=a-1
    i=i+1

# It will print last number of user
   
 