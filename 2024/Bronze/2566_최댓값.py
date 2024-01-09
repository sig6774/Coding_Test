table = [list(map(int, input().split())) for _ in range(9)]

# 0 ~ 90 사이의 값이 주어짐 
comparison_var = -1

# 행과 열 
row_num, col_num = 0, 0
for i in range(9):
    for j in range(9):
        if table[i][j] > comparison_var:
            comparison_var = table[i][j]
            row_num, col_num = i, j 
print(comparison_var)
print(row_num+1, col_num+1)