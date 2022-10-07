num=int(input("Enter the number: "))  
m=0  
for i in range(1,num):  
    if (num%i==0):  
        m=m+i  
if(m==num):  
    print(True)  
else:  
    print(False)