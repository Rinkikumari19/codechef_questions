N = int(input())
count = 0
while N > 0:
    d = N%10
    count = count + 1
    N = N//10
if count == 1:
    print('1')
elif count == 2:
    print('2')
elif count == 3:
    print('3')
else:
    print('More than 3 digits')


