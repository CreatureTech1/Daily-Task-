from datetime import *
from datetime import *
date=input("enter a date:")
print("the given date is:",date)
date_format='%d/%m/%Y'
date_obj=datetime.strptime(date, date_format)
n=7
my_date=date_obj-timedelta(days=n)
print("after sub a week from given date is:",my_date)