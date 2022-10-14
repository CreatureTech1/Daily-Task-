from random import randrange
min = 1
max = 49
num = 6
ticket_nums = []
for   i  in  range (num):
    rand_num = randrange(min, max+1)
    while    rand_num   in  ticket_nums:
        rand_num = randrange(min, max+1)
        ticket_nums.append(rand_num)
ticket_nums.sort()
print ("Your numbers are:   ",  end="")
for   i  in  ticket_nums:
   print (i, end=" ")
print ()