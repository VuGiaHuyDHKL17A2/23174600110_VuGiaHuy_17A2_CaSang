gia_tien=5000
so_gio=int(input("Nhập thời gian sử dụng máy lọc không khí:"))
cong_suat = 220*1.5 # W
cong_suat_doi = cong_suat/1000 # đổi W sang kW
gia_dien = cong_suat_doi *so_gio*gia_tien 
print("Số tiền phải trả là: {:.0f} đồng".format(gia_dien))