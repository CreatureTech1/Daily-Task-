list1 = ["Hello ", "take "] 
list2 = ["Dear", "Sir"]
my_list=[list1 + list2 for list1,list2 in zip(list1, list2)]
print(my_list)