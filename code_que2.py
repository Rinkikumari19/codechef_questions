T = int(input("enter you test cases number"))
for i in range(T):
    N = int(input("enter your number of students"))
    A = input()
    A = A.split()
    print(A)
    count = 0
    # if len(A)==N:
    index = 0
    while index < len(A):
        p = index+1
        while p<=(N-1):
            if A[index]== A[p]:
                count = count+1
            p=p+1
        index=index+1
    print(count)





    











