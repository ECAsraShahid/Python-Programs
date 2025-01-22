n=int(input("Enter the number of terms to find its sum:"))
sum=0
for i in range(1,n+1):
    sum+=i
print("The sum of first",n,"positive integers is:",sum)
