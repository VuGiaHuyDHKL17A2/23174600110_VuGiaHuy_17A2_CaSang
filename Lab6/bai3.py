n = int(input("Nhập số lượng phần tử trong dãy: "))
day_so = []
for i in range(n):
  so = (input(f"Nhập phần tử thứ {i + 1}: "))
  day_so.append(so)

so_lon_nhat = day_so[0]
so_nho_nhat = day_so[0]
for so in day_so:
  if so > so_lon_nhat:
    so_lon_nhat = so
  if so < so_nho_nhat:
    so_nho_nhat = so

print("Số lớn nhất:", so_lon_nhat)
print("Số nhỏ nhất:", so_nho_nhat)
