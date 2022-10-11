str=input("enter three city name:")
words = [word.lower() for word in str.split()]
words.sort()
print("the alphabetic order is:")
for word in words:
   print(word)