a = [1, 2, 3, 4, 5, 6,7,8,9]
for i, n in enumerate(a):
  if n % 2 != 0:
     a[i] = -1

print(a)