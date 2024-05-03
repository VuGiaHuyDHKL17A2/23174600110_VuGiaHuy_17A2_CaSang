sinh_vien_dict = {}
xep_loai_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

for _ in range(10):
    ten_sv = input("Nhập tên sinh viên: ")
    diem_thi = float(input(f"Nhập điểm thi của {ten_sv}: "))
    if diem_thi < 4.0:
        sinh_vien_dict[ten_sv] = 'F'
    elif diem_thi < 5.5:
        sinh_vien_dict[ten_sv] = 'D'
    elif diem_thi < 7.0:
        sinh_vien_dict[ten_sv] = 'C'
    elif diem_thi < 8.5:
        sinh_vien_dict[ten_sv] = 'B'
    else:  
        sinh_vien_dict[ten_sv] = 'A'
    xep_loai_count[sinh_vien_dict[ten_sv]] += 1

print("Thông tin xếp loại học lực của sinh viên:")
for ten_sv, xep_loai in sinh_vien_dict.items():
    print(f"Sinh viên {ten_sv} có xếp loại: {xep_loai}")

print("\nThống kê số lượng sinh viên theo mỗi xếp loại học lực:")
for xep_loai, so_luong in xep_loai_count.items():
    print(f"Xếp loại {xep_loai}: {so_luong}")