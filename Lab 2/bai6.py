a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
if a >= b and a >= c:
    so_lon_nhat = a
elif b >= a and b >= c:
    so_lon_nhat = b
else:
    so_lon_nhat = c
if a == so_lon_nhat:
    if b >= c:
        so_lon_thu_hai = b
    else:
        so_lon_thu_hai = c
elif b == so_lon_nhat:
    if a >= c:
        so_lon_thu_hai = a
    else:
        so_lon_thu_hai = c
else:
    if a >= b:
        so_lon_thu_hai = a
    else:
        so_lon_thu_hai = b
print("Số lớn thứ hai là:", so_lon_thu_hai)
