kho = {
 "banana": 6,
 "apple": 5,
 "orange": 32,
 "pear": 15
}

gia_tien = {
 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3
}

tong_so_tien_hoa_don = 0
hoa_don = []

# Tính toán hóa đơn
for mat_hang in kho:
    so_luong = kho[mat_hang]
    don_gia = gia_tien[mat_hang]
    so_tien = so_luong * don_gia
    tong_so_tien_hoa_don += so_tien
    hoa_don.append((mat_hang, so_luong, don_gia, so_tien))

# In thông tin hóa đơn
print("Hóa đơn mua hàng")
for mat_hang, so_luong, don_gia, so_tien in hoa_don:
    print(f"{mat_hang} - Số lượng: {so_luong} - Đơn giá: {don_gia} - Số tiền: {so_tien}")

# In tổng số tiền hóa đơn
print(f"Tổng số tiền hóa đơn: {tong_so_tien_hoa_don}")

# In lại số lượng của các mặt hàng trong kho
print("\nSố lượng mặt hàng trong kho sau khi mua:")
for mat_hang in kho:
    print(f"{mat_hang}: {kho[mat_hang]}")