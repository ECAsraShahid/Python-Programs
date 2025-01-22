n=int(input("Enter the number of rows to print the pattern:"))

a=1
for k in range(3,n+1):
    m=2*a-1
    a+=1
print(m)
for l in range(0,n*2-1):
    print('*',end='')
print()
for i in range(2,n+1):
    for j in range(1,n+1):
        if(i == j):
            print('*',end='')
            break
        else:
            print(' ',end='')
    if i<=(n-1) and m>=1:
        for p in range(0,m):
            print(' ',end='')
        m=m-2
        print('*')
    
        
