# Nhập dãy số từ người dùng
n = int(input("Nhập số lượng phần tử trong dãy: "))
day_so = [int(input(f"Nhập phần tử thứ {i + 1}: ")) for i in range(n)]

# Duyệt qua dãy số và kiểm tra sai số giữa các phần tử liên tiếp
i = 1
while i < n:
  if day_so[i] - day_so[i - 1] != day_so[1] - day_so[0]:
    print("Dãy số", day_so, "không phải là cấp số cộng.")
    break
  i += 1
else:
  # Nếu vòng lặp hoàn thành mà không bị ngắt bởi break, dãy số là cấp số cộng
  print("Dãy số", day_so, "là cấp số cộng.")