'''
year=int(input("enter the year: "))
month=input("enter the month: ")

if month == 'Feb':
    print("no.of.days : 28days")
elif month in ("April", "June", "September", "November"):
    print("no.of.days : 30days")
elif month in ("January", "March", "May", "July", "August", "October", "December"):
    print("no.of.days : 31days")
else:
    print(month,' is not a correct month name') 



major={'M':' Mathematics' , 'C': 'Computer Science' , 'I': 'Information Technology '}
status= {'1':'freshman','2':'sophomore','3':'junior','4':'senior'}
user=input("enter the two character :")
if user[0:1] in major and user[1:2] in status:
    print(major[user[0:1]],status[user[1:2]])
else:
    print("invalid userinput")





a=input("enter the string 1: ")
b=input("enter the string 2: ")

if b in a:
    print(b,'is a substring of',a)
else:
    print(b," is not a substring of ",a)
    

SSN=input("Enter SSN (ddd-dd-dddd):")
spc=SSN.split('-')
valid=False
if len(spc)==3:
    if len(spc[0])==3 and len(spc[1])==2 and len(spc[2])==4:
        valid = True
        print ("Valid Social Security Number")
    else:
        Invalid = False
        print("Invalid Social Security Number")  



employeeName = (input("Enter employee name: "))
hoursWorked = (input("Enter number of hours worked in a week: "))
payRate = (input("Enter hourly pay rate:  "))
grossPay= (input("Enter federal tax withholding rate :$ "))
deduction=(input("Enter deduction:$ ")) 
state = (input("Enter state tax withholding rate: "))
totaldeduction=(input("Enter Total deduction:$ "))
netpay=(input("Enter netpay=$ "))
print("Employee Name={}".format(employeeName))
print("Hours Worked={}".format(hoursWorked))
print("Pay Rate={}".format(payRate))
print("Gross Pay={}".format(grossPay))
print("Deduction:Federal withholding={}".format(deduction))
print("State with holding={}".format(state))
print("Total Deduction={}".format(totaldeduction))
print("Net pay={}".format(netpay))    



my_list =input("list of words that are comma seperates")
split=[x for x in my_list.split(',')]
split.sort()
print("user word sorted by alpha: ")
print(','.join(split)) 

Grade={'A':4 ,'B':3 ,'C':2 ,'D':1 ,'F':0}
a=input('enter the value')
if a not in Grade:
    print('invalid')
else:
    print('grade value ',Grade[a]) 

i=ord('e')
print(i)

 

a=[]
b=input('enter the string')
for i in range(len(b)):
    if i % 2 ==0:
        a.append(b[i])
print(a)


str_1 =str(input("enter the words: "))
str_2 = ''
vowels=0
for i in str_1:
    if i == 'a' or i== 'e' or i=='i' or i=='o' or i=='u':

        continue
    str_2 = str_2 + i
    vowels+=1
print("num of vowels: " ,vowels)
print(str_2)'''
























































 
