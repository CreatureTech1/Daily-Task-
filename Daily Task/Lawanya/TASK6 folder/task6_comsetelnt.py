num1={1,2,3,4,5}
num2={8,7,5,4,6}
num3={0,9}
print("check whether there is no common elements present")
print("is num1 and num2 has no common element:", num1.isdisjoint(num2))
print("is num1 and num2 has no common element:", num3.isdisjoint(num1))
print("is num1 and num2 has no common element:", num2.isdisjoint(num3))
