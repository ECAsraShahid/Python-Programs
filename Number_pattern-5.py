n=int(input("Enter the number of rows to print the pattern:"))

for i in range(1,n+1):
    for k in range(0,i-1):
        print(' ',end='')
    for j in range(i,n+1):
        print(j,end='')
    print()
