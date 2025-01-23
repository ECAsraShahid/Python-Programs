def main():
    num=1
    ArmStrong=[]
    while num<=1000:
        count=0
        collect=0
        
        for i in str(num):
           count+=1
        
        for i in str(num):
            collect+=int(i)**count
        
        if num==collect:
            ArmStrong.append(collect)
           
        num+=1
    return ArmStrong
x=main()
print(x)
