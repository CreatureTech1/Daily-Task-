from email.policy import default


name=input("enter your name")
sal=int(input("enter a number"))
def showemployee(default=9000):
    if sal!=0:
        print("employee name is", name)
        print("salary is", sal)
    else:
        print("employee name is", name)
        print("salary is", default)
showemployee()

