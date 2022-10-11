str=input("enter your string:")
vowels=0
constants=0
for i in str:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowels=vowels+1
    elif(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
    else:
        constants=constants+1
print("the number of vowels are:",vowels)
print("the number of constants are:",constants)


