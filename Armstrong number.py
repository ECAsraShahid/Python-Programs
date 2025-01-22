num=input("Enter the number to check whether it is an Armstrong Number or not:")

count=0
collect=0
for i in num:
   count+=1

for i in num:
    collect+=int(i)**count


if int(num)==collect:
    print("The given number is an Armstrong number.")
else:
    print("The given number is not an Armstrong number.")


