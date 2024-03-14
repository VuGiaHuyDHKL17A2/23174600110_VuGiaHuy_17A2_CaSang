x_M, y_M = map(float, input("Nhập tọa độ của điểm M (x, y): ").split())
x_N, y_N = map(float, input("Nhập tọa độ của điểm N (x, y): ").split())
x_P, y_P = map(float, input("Nhập tọa độ của điểm P (x, y): ").split())
x_Q, y_Q = map(float, input("Nhập tọa độ của điểm Q (x, y): ").split())

# Tính toán tọa độ trung điểm của mỗi cạnh
trungdiem_x_MN = (x_M + x_N) / 2
trungdiem_y_MN = (y_M + y_N) / 2

trungdiem_x_NP = (x_N + x_P) / 2
trungdiem_y_NP = (y_N + y_P) / 2

trungdiem_x_PQ = (x_P + x_Q) / 2
trungdiem_y_PQ = (y_P + y_Q) / 2

trungdiem_x_QM = (x_Q + x_M) / 2
trungdiem_y_QM = (y_Q + y_M) / 2

# In ra tọa độ trung điểm
print("Tọa độ trung điểm của cạnh MN:", (trungdiem_x_MN, trungdiem_y_MN))
print("Tọa độ trung điểm của cạnh NP:", (trungdiem_x_NP, trungdiem_y_NP))
print("Tọa độ trung điểm của cạnh PQ:", (trungdiem_x_PQ, trungdiem_y_PQ))
print("Tọa độ trung điểm của cạnh QM:", (trungdiem_x_QM, trungdiem_y_QM))
