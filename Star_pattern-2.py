n=int(input("Enter the number of rows to print the star pattern:"))
for i in range(n,0,-1):
    for k in range(0,n-i):
        print(' ',end='')
    for j in range(0,i*2-1):
        print('*',end='')
    print()
