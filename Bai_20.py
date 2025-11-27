matrix = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]
n = len(matrix)
tong_cheo_chinh = sum(matrix[i][i] for i in range(n))
tong_cheo_phu = sum(matrix[i][n - 1 - i] for i in range(n))
tuple_matrix = tuple(tuple(row) for row in matrix)

print("Tổng đường chéo chính:", tong_cheo_chinh)
print("Tổng đường chéo phụ:", tong_cheo_phu)
print("Ma trận dạng tuple:", tuple_matrix)
