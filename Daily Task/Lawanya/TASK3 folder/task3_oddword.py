a=[]
my_data=input("enter your string:")
for i in range(len(my_data)):
    if i % 2 != 0:
        a.append(my_data[i])
print(format(a))

