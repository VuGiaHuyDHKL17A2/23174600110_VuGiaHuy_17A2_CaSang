tong = 50
bi_do = 20
bi_xanh = 15
bi_vang = 15
a = int(input("Nhập số lượng viên bi bạn muốn rút: "))

# Xác suất tất cả là bi đỏ
xac_suat_bi_do = bi_do / tong

# Xác suất ít nhất một viên là bi xanh
xac_suat_it_nhat_mot_bixanh = 1 - (bi_do / tong)

# Xác suất đúng hai viên là bi vàng
xac_suat_hai_bivang = (bi_vang / tong) * ((bi_vang - 1) / (tong - 1))

# Hiển thị kết quả
print("Xác suất tất cả là bi đỏ: {:.4f}".format(xac_suat_bi_do))
print("Xác suất ít nhất một viên là bi xanh: {:.4f}".format(xac_suat_it_nhat_mot_bixanh))
print("Xác suất đúng hai viên là bi vàng: {:.4f}".format(xac_suat_hai_bivang))