n=int(input("Enter the number to get it's factorial:"))
fact=1
for i in range(2,n+1):
    fact=fact*i
print("The factorial of",n,"is",fact)  
