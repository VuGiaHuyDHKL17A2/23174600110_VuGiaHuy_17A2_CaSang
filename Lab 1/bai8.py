import math
x, z = map(float, input("Nhập hai số thực x và z: ").split())
f = (x**2*math.sin(z) + (abs(x))**0.5)/(math.log(z) + math.exp(x-1)) + math.atan(x*z)
print("({:.0f},{:.0f}) = {:.2f}".format(x,z,f))