str1 = input("Nhập vào chuỗi thứ nhất: ")
str2 = input("Nhập vào chuỗi thứ hai: ")
chuoi_gop = ""
min_length = 0
if len(str1) < len(str2):
    min_length = len(str1)
else:
    min_length = len(str2)
for i in range(min_length):
    chuoi_gop += str1[i] + "-" +str2[i] +"-"

#Xử lý phần còn lại của chuỗi dài hơn
if len(str1) < len(str2):
    chuoi_gop += str2[min_length:]
else:
    chuoi_gop += str1[min_length:]

print("Chuỗi trộn của hai chuỗi đã nhập là:", chuoi_gop[:-1])