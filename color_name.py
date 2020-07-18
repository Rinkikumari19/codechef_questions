data = ['red','orange','blue','green','white']
data2 = ['black','yellow','green','blue']
a = 0
data3 = []
while a < len(data):
    if data[a] not in data2:
        data3.append(data[a])
    a=a+1
b = 0
while b < len(data2):
    if data2[b] not in data3:
        data3.append(data2[b])
    b=b+1
print(data3)