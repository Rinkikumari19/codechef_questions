def fabb(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return(fabb(n-1)+fabb(n-2))
print(fabb(6))