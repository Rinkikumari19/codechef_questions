T = int(input())
for i in range(T):
    N = int(input())
    N1 = str(N)
    store = 0
    while N > 0:
        d = N%10
        store = (store*10)+d
        N = N // 10
    store = str(store)
    output = ("wins")
    for index in range(len(N1)):
        if N1[index] != store[index]:
            output = ('loses')
            break
    print(output)

