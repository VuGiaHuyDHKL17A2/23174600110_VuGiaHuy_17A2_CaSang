while True:
    chuoi = input("Nhập một chuỗi ký tự (ít nhất 10 ký tự): ")
    if len(chuoi) >= 10:
        break
    else:
        print("Chuỗi phải có ít nhất 10 ký tự. Vui lòng nhập lại.")


# a) Trích ra chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8
chuoi_con_a = chuoi[1:8]

# b) Trích ra chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5
chuoi_con_b = chuoi[4:9]

# c) Trích ra chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự
chuoi_con_c = chuoi[-3:]

# d) Chuyển đổi các ký tự trong chuỗi thành chữ thường
chuoi_thuong = chuoi.lower()

# e) Chuyển đổi các ký tự trong chuỗi thành chữ hoa
chuoi_hoa = chuoi.upper()

# f) Đảo ngược chuỗi ký tự
chuoi_dao_nguoc = chuoi[::-1]

# In kết quả
print(f"Chuỗi con từ vị trí 2 đến 8: {chuoi_con_a}")
print(f"Chuỗi con 5 ký tự từ vị trí 5: {chuoi_con_b}")
print(f"Chuỗi con 3 ký tự từ cuối chuỗi: {chuoi_con_c}")
print(f"Chuỗi sau khi chuyển sang chữ thường: {chuoi_thuong}")
print(f"Chuỗi sau khi chuyển sang chữ hoa: {chuoi_hoa}")
print(f"Chuỗi đảo ngược: {chuoi_dao_nguoc}")
