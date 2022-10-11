major={"M" : "Mathematics" , "C" : "Computer Science" , "I" : "Information Technology" }
year = {"1" : "Freshman", "2" :"Sophomore" , "3" : "Junior", "4" :"Senior"}

u=input("Enter two Characters: ")

if u[0:1] in major and u[1:2] in year:
    print(major[u[0:1]],year[u[1:2]])

