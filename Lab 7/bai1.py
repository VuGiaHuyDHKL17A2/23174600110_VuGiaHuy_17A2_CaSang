sinhvien = {}

N = int(input("Nhập số lượng sinh viên: "))

for i in range(1, N + 1):
    ten_sinh_vien = input(f"Nhập tên sinh viên thứ {i}: ")
    diem_sinh_vien = float(input(f"Nhập điểm cho sinh viên {ten_sinh_vien}: ")) 
    x3 = diem_sinh_vien ** 3
    sinhvien[ten_sinh_vien] = x3

print(sinhvien)