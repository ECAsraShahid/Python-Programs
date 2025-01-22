n=int(input("Enter the number of rows(should be odd) to print the pattern:"))

j=1
n=int((n-1)/2)
for i in range(n,-1,-1):
    for k in range(0,i):
        print(' ',end='')
    print('*'*j)
    j+=2
    
j-=4

for i in range(0,n):
    for k in range(0,i+1):
        print(' ',end='')
    print('*'*j)
    j-=2
