import re
my_id=input("enter your ssn:")
regex="^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$";
x=re.compile(regex)
if (re.search(x, my_id)):
    print("it is a valid number")
else:
    print("it is an invalid number")
        


