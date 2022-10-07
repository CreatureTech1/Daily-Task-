a=[]
n=int(input("Enter an integer:"))
print("The divisors of the number are:")
for i in range(1,n+1):
    if(n%i==0):
        a.append(i)
print(a)