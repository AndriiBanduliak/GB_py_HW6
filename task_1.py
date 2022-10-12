a = [15, 16, 2, 3, 1, 7, 5, 4, 10]
for i in range(len(a) - 1):
   n = [a[i]]
   i += 1
   m = [a[i]]
   if m > n:
       n = m
       print(m, end='\n') 