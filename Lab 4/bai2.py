# a) Viết chương trình in ra các số nguyên tố nhỏ hơn 100 (sử dụng vòng lặp while)
print("\na)")
so = 2
while so < 100:
    nguyen_to = True
    for i in range(2, so):
        if so % i == 0:
            nguyen_to = False
            break
    if nguyen_to:
        print(so,end=" ")
    so += 1


# b) Viết chương trình in ra các số chính phương nhỏ hơn 100 (sử dụng vòng lặp while)
print("\nb)")
so = 1
while so * so < 100:
    print(so * so, end=" ")
    so += 1


# c) Viết chương trình để in ra tất cả các số Fibonacci nhỏ hơn 1000 (sử dụng vòng lặp while)
print("\nc)")
a, b = 0, 1
while a < 1000:
    print(a, end=" ")
    a, b = b, a + b




