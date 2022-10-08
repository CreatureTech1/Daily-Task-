num=[3, 42, 9, 20]
for i in range(len(num)-1):
    if num[i] > num[i+1]:
        print(False)
    else:
        print(True)  
print(sorted(num))
     

