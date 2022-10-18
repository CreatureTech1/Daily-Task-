list=(50, 10, 60, 70, 50,80,90,50,60,70,50,70)
tuple=[[i,list.count(i)] for i in set(list)]
print(tuple)