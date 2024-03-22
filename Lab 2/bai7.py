chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))
bmi = can_nang / (chieu_cao * chieu_cao)
if bmi < 18.5:
    phan_loai = "Gầy"
elif 18.5 <= bmi < 25.0:
    phan_loai = "Bình thường"
elif 25.0 <=bmi < 30.0 :
    phan_loai = "Hơi béo"
else:
    phan_loai = "Béo"
print("Chỉ số BMI của bạn là:", bmi)
print("Phân loại BMI:", phan_loai)
