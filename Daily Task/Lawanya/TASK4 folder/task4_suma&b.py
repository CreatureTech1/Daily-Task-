from cmath import log10


a=int(input("enter a number"))
b=int(input("enter another numer"))
sum=a+b
sub=a-b
prod=a*b
quo=a/b
rem=a%b
res_1=log10(a)
res_2=log10(b)
print("sum of a and b is:", sum)
print("Difference when b is subtracted from a:", sub)
print("product of a and b:", prod)
print("quotient when a is divided by b is:", quo)
print("remainder when a is divided by b is:", rem)
print("result of log a is:", res_1)
print("result of log b is:", res_2)
