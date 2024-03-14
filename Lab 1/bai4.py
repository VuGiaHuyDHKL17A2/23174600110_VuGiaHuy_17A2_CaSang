a = float(input("Nhập độ dài cạnh đáy: "))
h = float(input("Nhập độ dài chiều cao: "))
Sd = a**2 
Sxq = (4 * a)*h/2
Stp = Sd + Sxq
V = (1/3) * Sd * h 
print("Diện tích xung quanh của hình chóp tứ giác đều là: {:.2f}".format(Sxq))
print("Diện tích toàn phần của hình chóp tứ giác đều là: {:.2f}".format(Stp))
print("Thể tích của hình chóp tứ giác đều là: {:.2f}".format(V))
