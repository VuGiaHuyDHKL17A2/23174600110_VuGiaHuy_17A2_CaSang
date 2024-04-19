# Nhập ma trận vuông
n = int(input("Nhập kích thước ma trận (n x n): "))
matrix = []
for i in range(n):
  row = []
  for j in range(n):
    row.append(int(input(f"Nhập phần tử [{i},{j}]: ")))
  matrix.append(row)

print("Ma trận đã nhập:")
for row in matrix:
  print(row)


# Ma trận đối xứng
ma_tran_chuyen_vi = [[matrix[j][i] for j in range(n)] for i in range(n)]
ma_tran_doi_xung = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != ma_tran_chuyen_vi[i][j]:
            ma_tran_doi_xung = False
            break
if ma_tran_doi_xung:
    print("Ma trận trên là ma trận đối xứng")
else:
    print("Ma trận không phải là ma trận đối xứng")


# Ma trận nghịch đảo
