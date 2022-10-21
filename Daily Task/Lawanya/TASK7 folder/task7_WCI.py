#import math
v= float(input("enter the wind speed in km/hr"))
t = float(input("enter the air temperature in degree celcius"))
chill_index = 35.12 + 0.6215*t - 11.37(v**0.16) + 0.3965*t(v**0.16)
print("the wind chill index is:", int(round(chill_index, 0)))