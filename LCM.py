num=[]
for i in range(2):
    n=int(input(f"Enter the the {i+1} element:"))
    num.append(n)
print(num)

def LowestCommonMultiple():
    mul=1
    i=2
    while(num[0]!=1 or num[1]!=1):
        if num[0]%i==0 or num[1]%i==0:
            if num[0]%i==0 and num[1]%i==0:
                num[0]=num[0]//i
                num[1]=num[1]//i
                mul=mul*i
            elif num[0]%i==0 and num[1]%i!=0:
                num[0]=num[0]//i
                mul=mul*i
            elif num[0]%i!=0 and num[1]%i==0:
                num[1]=num[1]//i
                mul=mul*i
        else:
             i+=1
    return mul

x=LowestCommonMultiple()
print("LCM:",x)
