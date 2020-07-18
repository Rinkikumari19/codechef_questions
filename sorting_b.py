
list1 = [-1,5,190,170,-1,-1,160,67]
for i in range (len(list1)):
    a = 0
    while a < len(list1)-1:
        if list1[a]>list1[a+1]:
            list1[a],list1[a+1] = list1[a+1],list1[a]
        a=a+1
  
print(list1)