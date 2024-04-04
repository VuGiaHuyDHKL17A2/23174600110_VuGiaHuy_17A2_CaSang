tiep_tuc = 'y'
while tiep_tuc.lower() == 'y':
    a, b = map(int, input("Nhập vào hai số a và b: ").split())
    
    print("""
    Chương trình hiển thị menu chọn phép toán:
    1. Phép cộng 2 số
    2. Phép trừ 2 số
    3. Phép nhân 2 số
    4. Phép chia 2 số
    5. Tính lũy thừa 2 số
    6. Tính căn bậc hai của hai số
    """)
    
    lua_chon = int(input("Nhập vào lựa chọn: "))
    
    if lua_chon == 1:
        print(f"Tổng 2 số là: {a} + {b} = {a + b}")
    elif lua_chon == 2:
        print(f"Hiệu 2 số là: {a} - {b} = {a - b}")
    elif lua_chon == 3:
        print(f"Tích 2 số là: {a} x {b} = {a * b}")
    elif lua_chon == 4:
        print(f"Thương 2 số là: {a} : {b} = {a / b}")
    elif lua_chon == 5:
        print(f"Lũy thừa: {a} ^ {b} = {a ** b}")
    elif lua_chon == 6:
        print(f"Căn bậc hai của số thứ nhất: √{a} = {a ** 0.5}")
        print(f"Căn bậc hai của số thứ hai: √{b} = {b ** 0.5}")
    else:
        print("Lựa chọn sai, vui lòng nhập lại.")
    
    tiep_tuc = input("Bạn có muốn tiếp tục không? (Nhập 'y' hoặc 'n'): ")

print("Chương trình kết thúc. Cảm ơn bạn đã sử dụng!")
