n = int(input("Nhập vào số lượng số nguyên dương n: "))
mang = []

for i in range(n):
    so = int(input(f"Nhập số nguyên thứ {i+1}: "))
    mang.append(so)

print("Các số nguyên tố trong mảng: ")
for so in mang:
    if so > 1:
        for i in range(2, so):
            if (so % i) == 0:
                break
        else:
            print(so)

print("Các số hoàn hảo trong mảng: ")
for so in mang:
    tong_uoc = 0
    for i in range(1, so):
        if so % i == 0:
            tong_uoc += i
    if tong_uoc == so:
        print(so)