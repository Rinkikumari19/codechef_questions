

T = int(input())
for i in range(T):
    value = input()
    print(value)
    b = (len(value))//2
    c = (len(value))-b
    if len(value)%2==1:
        l = []
        for start_index in range(b):
            l.append(value[start_index])
        l.sort()
        print(l)
        l2 = []
        for a in range (b):
            p = a+c
            p1 = value[p]
            l2.append(p1)
        l2.sort()
        print(l2)
        res = "YES"
        for palindrom_index in range(b):
            if l2[palindrom_index]!=l[palindrom_index]:
                res = "NO"
                break
        print(res)
    else:
        l = []
        for start_index in range(b):
            l.append(value[start_index])
        l.sort()
        print(l)
        l2 = []
        for a in range (b):
            p = a+c
            p1 = value[p]
            l2.append(p1)
        l2.sort()
        print(l2)
        res = "YES"
        for palindrom_index in range(b):
            if l2[palindrom_index]!=l[palindrom_index]:
                res = "NO"
                break
        print(res)

# LAPINDROME QUESTION