heights=[168,170,150,160,170,182,140,175,191,152,150]


    
def mean():
        length=len(heights)
        add=sum(heights)
        avg=add/length
        return avg
def median():
        length=len(heights)
        heights.sort()
        print("List arranged in ascending order:",heights)
        if length%2!=0:
            x=int((length+1)/2)
            mid=heights[x-1]
            return mid
        else:
            x=int(length/2)
            y=int((length+1)/2)
            mid=(heights[x-1]+heights[y])/2
            return mid
def mode():
        length=len(heights)
        count_dict={}
       
        for i in range(length):
            count_dict[heights[i]]=heights.count(heights[i])

        temp=max(count_dict.values())
        if temp==1:
            print("No Mode")
        else:
            for i in count_dict:
                if count_dict[i]==temp:
                    print("Mode:",i)
def variance():
        avg=int(mean())
        
        total_sum=0
        
        for i in heights:
            total_sum=total_sum+((i-avg)**2)
        var=total_sum/len(heights)
        return var
        
    
def standard_deviation():
        var=variance()
        std_dev=var**0.5
        return std_dev
    
     

x=mean()
print (x)
y=median()
print (y)
mode()
z=variance()
print (z)
p=standard_deviation()
print (p)
