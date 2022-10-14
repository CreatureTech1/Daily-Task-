list=[]
my_data=input("enter strings")
while True:
    if my_data != "":
        if my_data not in list:
            list.append(my_data)
    my_data=input("enter strings")   
    for i in list:
        print(i)
