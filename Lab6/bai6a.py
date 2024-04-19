matrix = []
m = int(input("Nhập vào số hàng: "))
n = int(input("Nhập vào số cột: "))
for i in range(m):
    row = []
    for j in range(n):
        phan_tu = int(input(f"Nhập giá trị phần tử thứ [{i},{j}]: "))
        row.append(phan_tu)
    matrix.append(row)
print(matrix)

# Tổng ma trận
sum = 0 
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        sum += matrix[i][j]
print("Tổng các phần tử trong ma trận A là:", sum)

# Tích 2 ma trận 
m2 = int(input("Nhập số hàng của ma trận thứ hai: "))
n2 = int(input("Nhập số cột của ma trận thứ hai: "))
if n != m2:
    print("Không thể nhân hai ma trận vì số cột của ma trận đầu tiên không bằng số hàng của ma trận thứ hai.")
else:
    matrix2 = []
    for i in range(m2):
        row = []
        for j in range(n2):
            row.append(int(input(f"Nhập phần tử [{i}][{j}]: ")))
        matrix2.append(row)

tich_ma_tran = [[0 for _ in range(n2)] for _ in range(m)]
for i in range(m):
        for j in range(n2):
            for k in range(n):
                tich_ma_tran[i][j] += matrix[i][k] * matrix2[k][j]
    
print("Tích của hai ma trận là:")
for row in tich_ma_tran:
        print(row)
# Ma trận chuyển vị
ma_tran_chuyen_vi = [[matrix[j][i] for j in range(m)] for i in range(n)]
print("Ma trận chuyển vị của ma trận ban đầu là: ")
for row in ma_tran_chuyen_vi:
    print(row)