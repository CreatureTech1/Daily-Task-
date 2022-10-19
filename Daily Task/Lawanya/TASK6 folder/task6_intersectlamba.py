a=[1, 2, 3, 5, 7, 8, 9, 10]
b=[1, 2, 4, 8, 9]
print(a)
print(b)
n = list(filter(lambda x : x in a, b))
print(n)
