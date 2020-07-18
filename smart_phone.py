N = int(input())
l = []
for i in range(N):
    a = int(input())
    l.append(a)
l.sort()
print(l)
index = 1
num = (l[0]*N)
while 1<N:
    K= N-1
    sum = l[index]*(K)
    if num<sum:
        num = sum
    index=index+1
    N=K
print(num)

# SMART PHONE