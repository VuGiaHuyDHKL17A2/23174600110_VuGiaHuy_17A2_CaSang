import random
import csv

def rut_so():
    return random.randint(1, 100)

def kiem_tra_ket_qua(so_du_doan, so_rut):
    return so_du_doan == so_rut

def tinh_xac_suat_trung_giai(so_du_doan, so_rut):
    return "100%" if kiem_tra_ket_qua(so_du_doan, so_rut) else '0%'

def main():
    so_lan_choi = int(input("Nhập số lần chơi (tối đa 5 lần): "))
    while so_lan_choi > 5:
        print("Số lần chơi của bạn đã vượt quá 5. Vui lòng nhập lại")
        so_lan_choi = int(input("Nhập số lần chơi (tối đa 5 lần): "))

    so_du_doan = set()  
    danh_sach_so_rut = []  
    xac_suat_dict = {i: 0 for i in range(1, 101)}  

    tien_thuong = 0

    for _ in range(so_lan_choi):
        so_du_doan_input = int(input("Nhập số dự đoán (từ 1 đến 100): "))
        if len(so_du_doan) < so_lan_choi:
            so_du_doan.add(so_du_doan_input)
    
    for _ in range(so_lan_choi):
        so_rut = rut_so()
        xac_suat_dict[so_rut] += 1
        danh_sach_so_rut.append(so_rut)
    
    with open('ket_qua.csv', 'w', newline='') as csvfile:
        ten_cot = ['So_du_doan', 'So_rut', 'Xac_suat_trung_giai']
        writer = csv.DictWriter(csvfile, fieldnames=ten_cot)
        writer.writeheader()
        for i, so_du_doan_item in enumerate(so_du_doan):
            if i < len(danh_sach_so_rut):
                xac_suat = tinh_xac_suat_trung_giai(so_du_doan_item, danh_sach_so_rut[i])
                writer.writerow({'So_du_doan': so_du_doan_item, 'So_rut': danh_sach_so_rut[i], 'Xac_suat_trung_giai': xac_suat})

    print("\nKết quả:")
    for i, so_du_doan_item in enumerate(so_du_doan):
        if i < len(danh_sach_so_rut):
            xac_suat = tinh_xac_suat_trung_giai(so_du_doan_item, danh_sach_so_rut[i])
            print(f"Số dự đoán: {so_du_doan_item}, Số rút: {danh_sach_so_rut[i]}, Xác suất trúng giải: {xac_suat}")
            if xac_suat == "100%":
                print("Bạn đã đoán đúng, chúc mừng bạn nhận được 1 triệu")
                tien_thuong += 1000000

    print(f"Tổng số tiền thưởng của bạn là: {tien_thuong} VND")

if __name__ == "__main__":
    main()
