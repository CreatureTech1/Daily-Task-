def sub_list(n):    
    list=[[]]
    for i in range(len(n)+1):
        for j in range(i):
            list.append(n[j: i])
    return list 
n1=[1, 2, 3]
print(sub_list(n1))       
