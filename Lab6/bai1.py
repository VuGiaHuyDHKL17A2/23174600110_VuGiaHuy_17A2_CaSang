n = int(input("Nhập số lượng số nguyên dương n: "))
mang = []

for i in range(n):
    so = int(input(f"Nhập số nguyên thứ {i+1}: "))
    mang.append(so)

tong_chan = 0
tong_le = 0
for so in mang:
    if so % 2 == 0:
        tong_chan += so
    else:
        tong_le += so

print(f"Tổng của các số chẵn trong mảng: {tong_chan}")
print(f"Tổng của các số lẻ trong mảng: {tong_le}")