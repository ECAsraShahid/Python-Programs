n=int(input("Enter the number of rows to print the star pattern:"))
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(' ',end='')
    for k in range(0,i):
        print('*',end='')
    print()
