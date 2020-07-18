
T = int(input())
for i in range(T):
    S = input()
    b = (len(S))//2
    c = (len(S))-b
    l = [] 
    for a in range (b):
        p = a+c
        p1 = S[p]
        l.append(p1)
    if l[0]==S[0]:
        index2 = 0
        res1 = "YES"
        while index2 < (b):
            if S[index2]==l[index2]:
                index2=index2 + 1
            else:
                res1 = "NO"
                break  
        print(res1) 
    else: 
        l.reverse()
        index = 0
        res = "YES"
        while index < (b):
            if S[index]==l[index]:
                index=index+1
            else:
                res = "NO"
                break
        print(res)
# lepindrome question