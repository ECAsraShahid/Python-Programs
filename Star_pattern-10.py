n=int(input("Enter the number of rows(should be odd) to print the pattern:"))
a=1
for i in range(3,n+1,2):
    m=2*a-1
    a+=1
n=int((n-1)/2)
a=1
for i in range(n,-1,-1):
    for j in range(i,0,-1):
        print(' ',end='')
    if i==n:
        print('*')
    else:
        print('*',end='')
   
    
    if i<n and a<=m:
        for k in range(0,a):
            print(' ',end='')
        a+=2
        print('*')
a=m-2

for i in range(1,n+1):
    
    for j in range(0,i):
        print(' ',end='')
    print('*',end='')
    for k in range(a,0,-1):
        print(' ',end='')
    a-=2
    if i<n:
        print('*')
