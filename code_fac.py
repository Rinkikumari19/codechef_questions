T = int(input())
for i in range(T):
    count = 0
    user = int(input())
    num = 5
    while user >= num: 
        a = user//num
        count = count + a
        num=num*5
    print(count)


# input
# 6
# 3
# 60
# 100
# 1024
# 23456
# 8735373
# Sample Output:

# 0
# 14
# 24
# 253
# 5861
# 2183837


