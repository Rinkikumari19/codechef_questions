T = int(input("any number"))
for i in range(T):
    # hardness,carbon,tensil  = map(int, input().split())
A = input()
A = A.split()
hardness = int(A[0])
carbon = float(A[1])
tensil = int(A[2])
if hardness>50 and carbon<0.7 and tensil>5600:
    print(10)
elif hardness>50 and carbon<0.7 and tensil<=5600:
    print(9)
elif hardness<=50 and carbon<0.7 and tensil>5600:
    print(8)
elif hardness>50 and carbon>=0.7 and tensil>5600:
    print(7)
elif hardness>50 or carbon<0.7 or tensil>5600:
    print(6)
else:
    print(5)