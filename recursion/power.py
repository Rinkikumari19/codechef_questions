
user = int(input())
for i in range(user):
    def pow(a,b):
        if b == 0:
            return 1
        return(a*(pow(a,b-1)))
    a,b = map(int, input().split())
    print(pow(a,b))