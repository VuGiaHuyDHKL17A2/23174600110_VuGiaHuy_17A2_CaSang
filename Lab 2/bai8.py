a1, b1 = map(float, input("Nhập hệ số góc và hệ số tự do của đường thẳng thứ nhất: ").split())
a2, b2 = map(float, input("Nhập hệ số góc và hệ số tự do của đường thẳng thứ nhất: ").split())
if a1 == a2 and b1 == b2:
    print("Hai đường thẳng trùng nhau")
elif a1 == a2:
    print("Hai đường thẳng song song")
elif a1*a2==-1:
    print("Hai đường thẳng vuông góc")
else:
    print("Hai đường thẳng cắt nhau")