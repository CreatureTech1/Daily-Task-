from http.client import FOUND


num=[0, -1, 2, -3, 1]
n=len(num)
def sumthreenum(num, n):
    found = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (num[i] + num[j] + num[k] == 0):
                    print(num[i],num[j],num[k])
                    found = True
    if (found == False):
        print(" don't exist")
sumthreenum(num, n)