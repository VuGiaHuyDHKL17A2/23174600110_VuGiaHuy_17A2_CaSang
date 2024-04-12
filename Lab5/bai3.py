chuoi_van_ban = input("Nhập một chuỗi văn bản: ")
tu_can_tim = input("Nhập từ cần tìm kiếm: ")
dem_tu={}
so_lan_xuat_hien_nhieu_nhat=0
tu_xuat_hien_nhieu_nhat = ""

# Tìm vị trí của từ trong chuỗi
vi_tri = chuoi_van_ban.find(tu_can_tim)
if vi_tri != -1:
    print(f"Từ '{tu_can_tim}' xuất hiện tại vị trí {vi_tri} trong chuỗi.")
else:
    print(f"Từ '{tu_can_tim}' không xuất hiện trong chuỗi.")

for tu in chuoi_van_ban.split():
  dem_tu[tu] = dem_tu.get(tu, 0) + 1
  if dem_tu[tu] > so_lan_xuat_hien_nhieu_nhat:
    so_lan_xuat_hien_nhieu_nhat = dem_tu[tu]
    tu_xuat_hien_nhieu_nhat = tu
print(f"Từ xuất hiện nhiều nhất trong chuỗi là '{tu_xuat_hien_nhieu_nhat}'.")