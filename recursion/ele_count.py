list1 = []
def count_x(list,x,i):
    if x == list[i]:
        list1.append(list[i])
    if (len(list)-1) > i:
        count_x(list,x,i+1)
list = [4,5,6,4,4,3,5]
count_x(list,4,0)

print(len(list1))