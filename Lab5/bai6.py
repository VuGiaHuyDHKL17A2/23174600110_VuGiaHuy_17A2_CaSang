chuoi = input("Nhập một chuỗi văn bản: ")
so_ky_tu_dac_biet = 0
for i in chuoi:
    # Kiểm tra xem ký tự có phải là ký tự đặc biệt (không phải chữ hoặc số) hay không
    if not i.isalnum():
        so_ky_tu_dac_biet += 1
        
tong_so_ky_tu = len(chuoi)
ty_le_ky_tu_dac_biet = (so_ky_tu_dac_biet / tong_so_ky_tu) * 100

print(f"Số ký tự đặc biệt trong chuỗi: {so_ky_tu_dac_biet}")
print(f"Tỷ lệ phần trăm ký tự đặc biệt trong chuỗi: {ty_le_ky_tu_dac_biet:.2f}%")
