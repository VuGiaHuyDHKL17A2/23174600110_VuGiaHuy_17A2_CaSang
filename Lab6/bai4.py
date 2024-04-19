# a) Tạo danh sách Fibonacci
n = int(input("Nhập vào số n để tạo danh sách n số Fibonacci đầu tiên: "))
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(2,n + 1)]
print(f"{n} số đầu tiên của dãy Fibonacci:")
print(fibonacci[:n])


# b) Tạo danh sách số nguyên tố
nguyen_to = [True] * 100
for i in range(2, int(100 ** 0.5) + 1):
    if nguyen_to[i]:
        for i in range(i*i, 100, i):
            nguyen_to[i] = False
danh_sach_nguyen_to = [i for i in range(2, 100) if nguyen_to[i]]
print("Danh sách các số nguyên tố nhỏ hơn 100:")
print(danh_sach_nguyen_to)