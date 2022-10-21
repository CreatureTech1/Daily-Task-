import math
a=int(input("enter an interger"))
b=int(input("enter an interger"))
c=int(input("enter an interger"))
quad_func = (b ** 2) - (4 * a * c)
n1 = (-b-math.sqrt(quad_func))/(2*a)
n2 = (-b+math.sqrt(quad_func))/(2*a)
print("the 2 roots are:",n1,n2)