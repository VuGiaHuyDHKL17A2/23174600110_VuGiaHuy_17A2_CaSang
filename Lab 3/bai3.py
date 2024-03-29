# Câu a : In ra các số nguyên tố từ 100 đến 1000 (kể cả số 1000)
for i in range(100, 1001):
    nguyen_to = True
    for j in range(2, i):
        if i % j == 0:
            nguyen_to = False
    if nguyen_to:
        print(i,end=",")

# Câu b:In ra các số chính phương từ 1 đến 1000 (kể cả số 1000)
for i in range(1, 32):
    print(i ** 2, end=",")

# Câu c
a, b = 0, 1
for i in range(1,1000):
    if a < 100:
      print(a,end=",")
    a, b = b, a + b

# Câu d
tong_uoc=1
for i in range(2, 500):
   for j in range(2, i):
     if i % j == 0:
       tong_uoc += j
   if tong_uoc == i:
     print(i,end=",")

# Câu e
tong = 0
for n in range(1, 67):
  so_ngu_giac = (3 * n * n - n) // 2
  if so_ngu_giac <= 200:
    tong += so_ngu_giac
print(tong)







