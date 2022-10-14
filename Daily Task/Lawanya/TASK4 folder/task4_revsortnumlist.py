list= []
while True:
    number = int(input("Enter a number: "))
    if number != 0:
        list.append(number)
    else:
        list.sort(key=int, reverse=True)
        for i in list:
            print(i) 
 
