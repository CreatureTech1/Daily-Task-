'''
n=int(input("enter a positive integer:"))
sum=n*(n+1)/2
print("sum of the first", n , "positive integers are:", sum)



a=int(input("enter a number"))
b=int(input("enter another numer"))
sum=a+b
sub=a-b
prod=a*b
quo=a/b
rem=a%b
res_1=log10(a)
res_2=log10(b)
print("sum of a and b is:", sum)
print("Difference when b is subtracted from a:", sub)
print("product of a and b:", prod)
print("quotient when a is divided by b is:", quo)
print("remainder when a is divided by b is:", rem)
print("result of log a is:", res_1)
print("result of log b is:", res_2)



rad=int(input("enter the radius"))
pi=3.14
circle=pi*rad**2
sphere=(4/3)pi*rad*2
print("the area of a circle is:", circle)
print("the volume of a sphere is:", sphere)



b=int(input("enter the length"))
h=int(input("enter the height"))
triangle = b*h/2
print("the area of triangle with base length b and height h is:", triangle)




 cel=int(input("enter the degree"))
farehnite= (9/5)*cel +32
kelvin= cel + 273.15
print("the equivalent temperature in degree farehnite is:",farehnite,"F")
print("the equivalent temperature in degree kelvin is:",kelvin,"K")




n=int(input("enter four-digit number"))
x= n // 1000
x1 = (n - x*1000)//100
x2 = (n - x*1000 - x1*100)//10
x3 = n - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)




num1 = int(input("enter first integer"))
num2 = int(input("enter second integer"))
num3 = int(input("enter third integer"))
a=min(num1, num2, num3)
c=max(num1, num2, num3)
b=(num1+num2+num3)-a-c
print("the smallest number is:",a)
print("the largest number is:",b)
print("the middle number is:",c)
print("the sorted number is:",a,b,c)



sec_per_min=60
sec_per_hour=3600
sec_per_day=86400
days=int(input("enter no. of days"))
hours=int(input("enter no. of hours"))
min=int(input("enter no. of minutes"))
sec=int(input("enter no. of seconds"))
tot_sec= days * sec_per_day
tot_sec= tot_sec + (hours * sec_per_hour)
tot_sec= tot_sec + (min * sec_per_min)
tot_sec= tot_sec * sec
print("total no. of seconds:","%d"%(tot_sec))




radius=int(input("enter the radius"))
height=int(input("enter the height"))
pi=3.14
vol_of_cyl=pi*radius**2*height
print("the volume of cylinder is:",int(vol_of_cyl))





a=[]
while True:
    num=int(input("enter the numbers"))
    if num != 0:
        a.append(num)
    else:
        a.sort()
        for i in a:
            print (i)

 list= []
while True:
    number = int(input("Enter a number: "))
    if number != 0:
        list.append(number)
    else:
        list.sort(key=int, reverse=True)
        for i in list:
            print(i)


list=[]
my_data=input("enter strings")
while True:
    if my_data != "":
        if my_data not in list:
            list.append(my_data)
    my_data=input("enter strings")   
    for i in list:
        print(i)




neg=[]
zero=[]
pos=[]
num=int(input("enter an integer"))
while num != " ":
    if num < 0:
        neg.append(num)
    elif num > 0:
        pos.append(num)
    else:
        zero.append(num)
    num=int(input("enter an integer"))
    print(" the numbers are:")
    for i in neg:
        print(i)
    for i in pos:
        print(i)
    for i in zero:
        print(i)       




sum=0.0
count=0
num=1
while num != 0: 
    a=float(input("enter the number"))
    sum+=num
    count+=1
    sum=sum/count-1
    if count==0:
        print("add some more numbers")
    else:
        print("the avg of the above number is:",sum)



from random import randrange
min = 1
max = 49
num = 6
ticket_nums = []
for   i  in  range (num):
    rand_num = randrange(min, max+1)
    while    rand_num   in  ticket_nums:
        rand_num = randrange(min, max+1)
        ticket_nums.append(rand_num)
ticket_nums.sort()
print ("Your numbers are:   ",  end="")
for   i  in  ticket_nums:
   print (i, end=" ")
print ()    '''


        
