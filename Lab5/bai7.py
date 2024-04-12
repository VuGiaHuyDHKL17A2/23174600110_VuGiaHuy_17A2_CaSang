chuoi = input("Nhập chuỗi: ")
so_luong_chu_thuong = 0
so_luong_chu_hoa = 0
so_luong_chu_so = 0
so_luong_ky_tu_dac_biet = 0

for char in chuoi:
  if char.islower():
    so_luong_chu_thuong += 1
  elif char.isupper():
    so_luong_chu_hoa += 1
  elif char.isdigit():
    so_luong_chu_so += 1
  else:
    so_luong_ky_tu_dac_biet += 1

print(f"Số lượng chữ thường: {so_luong_chu_thuong}")
print(f"Số lượng chữ hoa: {so_luong_chu_hoa}")
print(f"Số lượng chữ số: {so_luong_chu_so}")
print(f"Số lượng ký tự đặc biệt: {so_luong_ky_tu_dac_biet}")

