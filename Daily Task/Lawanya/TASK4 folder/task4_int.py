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