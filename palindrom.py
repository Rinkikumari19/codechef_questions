name = ["n","i","t","i","n"]
b = -len(name)-1
i = -1
list = []
while i > b:
    list.append (name[i])
    i = i-1
print (list)
print (name)
i = 0
length = len(list)
while i < length:
    if name[i]==list[i]:
        print("palindrome hai")
    else:
        print("palindrome nhi hai")
    i = i+1