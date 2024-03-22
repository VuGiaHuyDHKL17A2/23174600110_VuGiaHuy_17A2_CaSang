print("Các thể loại phim : Hành động, Kinh dị, Tình cảm, Hài hước, Hoạt hình")
the_loai = input("Nhập thể loại phim bạn muốn xem: ")
thoi_gian = input("Nhập thời gian muốn xem phim (sáng, trưa, chiều, tối): ")
if the_loai== "tình cảm" and thoi_gian == "tối":
    print("Phim tình cảm sẽ được chiếu vào buổi tối")
elif the_loai == "hoạt hình" and (thoi_gian == "sáng" or thoi_gian == "trưa"):
    print("Phim hoạt hình sẽ được chiếu vào buổi sáng và trưa")
elif the_loai == "kinh dị" and thoi_gian == "tối":
    print("Phim kinh dị sẽ được chiếu vào buổi tối")
else:
    print("Không có suất chiếu")
