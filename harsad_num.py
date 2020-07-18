def is_harsad_number(number):
    a = str(number)
    b=0
    for i in range (len(a)):
        b=b+int(a[i])
    if number%b==0:
        print("harsad number hai")
    else:
        print("harsad number nahi h")
is_harsad_number(212)
# ye for loop se kiya h

            
def is_harsad_number(number):
    a = str(number)
    i=0
    b=0
    while i < len(a):
        b=b+int(a[i])
        i=i+1
    if number%b==0:
        print("harsad number hai")
    else:
        print("harsad number nhi h")
is_harsad_number(42)

