def tri_pat(size):
  k = n - 1
  for i in range(0,n):
    for j in range(0,k):
      print(end = " ")
    k -= 1
    for j in range (0, i+1):
      print("1 ", end='')
    print("\n") 

n = int(input())
tri_pat(n)