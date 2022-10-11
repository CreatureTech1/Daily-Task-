marks={"A" : 4, "B": 3, "C" : 2, "D" : 1, "E" : 0}

i = input("Enter a letter grade:")

if i not in marks:
    print("invalid Input")

else:
    print("The numeric value for grade", i,"is",marks[i])