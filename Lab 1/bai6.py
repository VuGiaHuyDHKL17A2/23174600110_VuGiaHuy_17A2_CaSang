import math
xa,ya = map(float,input("Nhập toạ độ của vecto a :").split())
xb,yb = map(float,input("Nhập toạ độ của vecto b :").split())
# 1.Phép cộng vecto a + b, phép trừ vecto a – b 
cong_x_vecto = xa + xb
cong_y_vecto = ya + yb
tru_x_vecto = xa - xb
tru_y_vecto = ya - yb
print(f"Phép cộng vecto a+b là: {cong_x_vecto, cong_y_vecto}")
print(f"Phép trừ vecto a-b là: {tru_x_vecto, tru_y_vecto}")

#2.Độ dài của vecto a, độ dài của vecto b 
do_dai_a = math.sqrt(xa**2+ya**2)
do_dai_b = math.sqrt(xb**2+yb**2)
print("Độ dài của vecto a là: ", do_dai_a)
print("Độ dài của vecto b là: ", do_dai_b)

# 3.Cosin góc hợp giữa hai vecto a và b (làm tròn đến 2 chữ số thập phân)
cosin=(xa*ya+xb*yb)/(do_dai_a*do_dai_b)
print("Cosin góc hợp giữa hai vecto a và b là: {:.2f}".format(cosin))
