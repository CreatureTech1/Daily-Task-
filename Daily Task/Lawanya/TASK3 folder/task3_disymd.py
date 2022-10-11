from tkinter.tix import DisplayStyle


class solution(object):
    def no_of_days(self,year,mon):
        leap=0
        if (year%400)==0:
            leap=1 
        elif (year%100)==0:
            leap=0 
        if mon==2:
            return 28 + leap
        m_lst=[1,3,5,7,8,10,12]
        if mon in m_lst:
            return 31 
        return 30 
x=solution()
year=int(input("enter the year:"))
mon=(input("enter the month:"))
cap=mon.capitalize()
if mon!=cap:
    print("this is not a correct month")
else:
    print(cap)
print(year)
print(x.no_of_days(2020, 2))

