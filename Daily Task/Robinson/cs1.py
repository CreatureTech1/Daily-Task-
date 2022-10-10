for i in range (6):
    for j in range (i):
        print("*",end=" ")           #program 1
    print(" ")
print("--------------------------")

n=6
for i in range (1,n):
    for j in range (n):              #program 4
        print(i,end=" ")
    print("")
print("--------------------------")


n=6
for i in range (n):
    for j in range (1,n):           #program 5
        print(j,end=" ")
    print("")
print("--------------------------")



n=6                                  #program 3
for i in range (n):
    for j in range (i):
        print(i,end=" ")
    print("")
print("--------------------------")


n=5
for i in range (1,n+1):
    for j in range (1,i+1):           #program 2
        if j==2 or j==4:
            print("*",end=" ")
        else:
            print(j,end=" ")

        
    print()
