diem_so = float(input("Nhập điểm số bài kiểm tra: "))
if diem_so < 0 or diem_so > 10:
  print("Điểm số không hợp lệ.")
else:
  if diem_so <= 5:
    print("Điểm kém.")
  elif diem_so <= 7:
    print("Điểm trung bình.")
  elif diem_so <= 8.5:
    print("Điểm khá.")
  else:
    print("Điểm tốt.")