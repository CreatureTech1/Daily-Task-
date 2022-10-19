n=int(input("enter an integer"))
def ord(num):
    if 4 <= n <= 20:
        suffix = 'th'
        print(str(n) + suffix)
    elif n == 1 or (n % 10) == 1:
        suffix = 'st'
        print(str(n) + suffix)
    elif n == 2 or (n % 10) == 2:
        suffix = 'nd'
        print(str(n) + suffix)
    elif n == 3 or (n % 10) == 3:
        suffix = 'rd'
        print(str(n) + suffix)
    elif n < 100:
        suffix = 'th'
        print(str(n) + suffix)
ord(n)
    