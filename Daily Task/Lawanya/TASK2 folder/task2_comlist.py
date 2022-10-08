def com_list(num1, num2):
    for i in num2:
        if i in num1:
            return True
    return False        
print(com_list([2, 3, 5], [4, 3, 6]))
print(com_list([2, 3, 5], [8, 7, 9]))