name = {5:6,2:76,3:1}
l = []
for i in name:
    l.append(i)
print(l) 
for a in range(len(l)-1):
    if l[a]>l[a+1]:
        l[a],l[a+1]=l[a+1],l[a]
for index in range(len(l)):
    print(l[index]) 


