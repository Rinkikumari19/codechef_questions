

T = int(input())
for i in range(T):
    user = input()
    user = user.split()
# print(user)
    C = int(user[0])
    D = int(user[1])
    L = int(user[2])
    E = (C+D)*4
    A = D*2 
    if C>=A:
        B = (C-A)*4+D*4
    else:
        B = D*4
    if B<=L and E>=L and L%4==0:
        print("yes")
    else:
        print("no")
# CATS DOGS LEG