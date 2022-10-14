a=[]
while True:
    num=int(input("enter the numbers"))
    if num != 0:
        a.append(num)
    else:
        a.sort()
        for i in a:
            print (i)
            

