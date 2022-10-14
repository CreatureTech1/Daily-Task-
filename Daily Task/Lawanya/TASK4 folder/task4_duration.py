sec_per_min=60
sec_per_hour=3600
sec_per_day=86400
days=int(input("enter no. of days"))
hours=int(input("enter no. of hours"))
min=int(input("enter no. of minutes"))
sec=int(input("enter no. of seconds"))
tot_sec= days * sec_per_day
tot_sec= tot_sec + (hours * sec_per_hour)
tot_sec= tot_sec + (min * sec_per_min)
tot_sec= tot_sec * sec
print("total no. of seconds:","%d"%(tot_sec))