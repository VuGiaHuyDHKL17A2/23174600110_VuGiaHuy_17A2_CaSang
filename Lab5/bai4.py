chuoi_ky_tu = input("Nhập chuỗi ký tự: ")
chuoi_so = ""
for i in chuoi_ky_tu:
    if i.isnumeric():
        chuoi_so += i
chuoi_ky_tu = chuoi_so

if chuoi_ky_tu:  
    so = int(chuoi_ky_tu)
    so_nguyen_to = True  
    if so <= 1:
        so_nguyen_to = False
    else:
        for i in range(2, so):
            if so % i == 0:
                so_nguyen_to = False
                break  
    print("Chuỗi sau khi loại bỏ ký tự không phải số:", chuoi_ky_tu)
    if so_nguyen_to:
        print(f"{so} là số nguyên tố")
    else:
        print(f"{so} không phải là số nguyên tố")

