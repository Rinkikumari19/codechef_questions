# Q3
def sum(n):
    if n==0:
        return n
    d = n%10
    return(d+sum(n//10))
print(sum(56334))