n=int(input("Enter the number of terms of fibonacci series you want:"))

num1=0
num2=1
if n==1:
    print(num1)
elif n==2:
    print(num1,"\n",num2)
else:
    print(num1,"\n",num2)
    for i in range(n-1):
        num3=num2+num1
        print(num3)
        num1=num2
        num2=num3
        
   
