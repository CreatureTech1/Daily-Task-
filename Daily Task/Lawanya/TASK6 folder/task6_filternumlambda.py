num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num)
a = list(filter(lambda x :x % 2 ==0, num))
print(a)
b = list(filter(lambda x : x % 2 != 0, num))
print(b)