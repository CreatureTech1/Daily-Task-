n=int(input("enter four-digit number"))
x= n // 1000
x1 = (n - x*1000)//100
x2 = (n - x*1000 - x1*100)//10
x3 = n - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)

