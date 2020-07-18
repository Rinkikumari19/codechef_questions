l = []
i=0
while i<10:
    user = int(input("enter your number"))
    l.append(user)
    i=i+1
p = l[1]-l[0]
a=0
while a<len(l)-1:
    if l[a]==l[a+1]-p:
        a=a+1
    else:
        print("conscetive progress number nhi hai")
        break
else:
    print("consective progressive number hai") 

# distance equale it will check between elements





