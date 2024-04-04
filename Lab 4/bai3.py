# Viết chương trình nhập vào một số nguyên và in ra số chữ số của số nguyên đó (sử dụng vòng lặp while).
so = int(input("Nhập số nguyên: "))
so_chu_so = 0
while so > 0:
    so =so//10
    so_chu_so += 1
print("Số chữ số của số nguyên:", so_chu_so)

