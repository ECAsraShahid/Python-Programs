r1=int(input("Enter the number of rows for first Matrix:"))
c1=int(input("Enter the number of columns for first Matrix:"))
p=[]
for i in range(r1):  #Getting Elements For First Matrix
    n=[]
    for j in range(c1):
        elements=int(input("Enter the Elements:"))
        n.append(elements)
    p.append(n)
print("<---First Matrix--->")   #Printing First Matrix
for i in p:
    print(i)
        
c2=int(input("Enter the number of columns for second Matrix:"))
q=[]
for i in range(c1):  #Getting Elements For Second Matrix
    n=[]
    for j in range(c2):
        elements=int(input("Enter the Elements:"))
        n.append(elements)
    q.append(n)
print("<---Second Matrix--->")  #Printing Second Matrix

for i in q:
    print(i)
r=[]
for i in range(r1): #Calculating Multiplication and Storing in a Third Matrix
    n=[]
    for j in range(c2):
        elements=0
        for k in range(c1):
            elements+=p[i][k]*q[k][j]
        n.append(elements)
    r.append(n)
print("<---Multiplication Of Matrix--->")
for i in r: #Printing Resultant Matrix

    print(i)
        
    
            


