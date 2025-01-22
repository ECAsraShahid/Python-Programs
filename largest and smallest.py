n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))
if (n1>n2) and (n1>n3):
    print(n1,"is greatest")
    if n2>n3:
        print(n3,"is smaller")
    else:
         print(n2,"is smaller")
elif (n2>n1) and (n2>n3):
    print(n2,"is greatest")
    if n1>n3:
        print(n3,"is smaller")
    else:
         print(n1,"is smaller")
else:
    print(n3,"is greatest")
    if n1>n2:
        print(n2,"is smaller")
    else:
         print(n1,"is smaller")
