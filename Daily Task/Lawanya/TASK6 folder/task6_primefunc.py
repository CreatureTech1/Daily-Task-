n=int(input("enter an integer"))
def prime(x):
    flag=False
    if n>1:
        for i in range(2,n):
            if n%i==0:
                flag=True
    if flag is True:
        print("it is not a prime no.")
    else:
        print("it is a prime no.")
prime(n)