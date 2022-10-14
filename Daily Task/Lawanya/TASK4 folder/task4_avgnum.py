sum=0.0
count=0
num=1
while num != 0: 
    a=float(input("enter the number"))
    sum+=num
    count+=1
    if count==0:
        print("add some more numbers")
    else:
        print("the avg of the above number is:",sum/(count-1),sum)
