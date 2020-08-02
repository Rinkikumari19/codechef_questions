
# Q2
def fac(sum):
    if sum == 1:
        return 1
    return(sum+fac(sum-1))
print(fac(5))
