"""
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true
Example 2:

Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false

"""

"""
1. 행과, 열 탐색 함수 생성 
2. 1*3 4*6 7*9 형태의 탐색 함수 생성 
3. 함수에는 ""을 제외하고 기존 데이터의 개수와 set을 했을 때 데이터 개수가 다르면 False 기능 포함
"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        def check_row(check_board : list[list[str]]) -> bool:
            flag = True
            for row_num in check_board:
                li = [] 
                for row_ele in row_num:
                    if row_ele != ".":
                        li.append(row_ele)
                lst_num = len(li)
                set_num = len(set(li))

                if lst_num != set_num:
                    flag = False
            
            return flag
        
        def check_col(check_board : list[list[str]]) -> bool:
            flag = True
            
            transpose_lst = [list(x) for x in zip(*check_board)]

            for row_num in transpose_lst:
                li = [] 
                for row_ele in row_num:
                    if row_ele != ".":
                        li.append(row_ele)
                lst_num = len(li)
                set_num = len(set(li))

                if lst_num != set_num:
                    flag = False
            
            return flag
        
        def isBox(x, y, num) -> bool:
            # 박스 가로, 세로 시작점
            boxX = x - (x % 3)
            boxY = y - (y % 3)

            for i in range(3):
                for j in range(3):
                    if ((boxX + i != x) and (boxY + j != y)) and board[boxX + i][boxY + j] != "." and board[boxX + i][boxY + j] == num:
                        return False

            return True

        flag_col, flag_row = check_col(board), check_row(board)
        if flag_col and flag_row:
            for i in range(9):
                for j in range(9):
                    flag = isBox(i,j, board[i][j])
                    print(flag)
                    if flag == False:
                        return False
        else:
            return False
            
        return True 
                
"""
두번째 요소를 3으로 나눴을 때 나머지가 2일 때 첫번째 요소 +1 
초기 빈 리스트에서 값을 넣었을 때 리스트에 9개의 값이 있을 때 두번째 요소를

11 12 13
21 22 23
31 32 33
14 15 16 
24 25 26
34 35 36
17 18 19
27 28 29
37 38 39
41 42 43
51 52 53 
61 62 63
"""
        



board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

board=[ ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
a = Solution()
print(a.isValidSudoku(board))
# for n in board:
#     print(n)
# def check_row(check_board : list[list[str]]) -> bool:
#     flag = True
#     for row_num in check_board:
#         li = [] 
#         for row_ele in row_num:
#             if row_ele != ".":
#                 li.append(row_ele)
#         lst_num = len(li)
#         set_num = len(set(li))

#         if lst_num != set_num:
#             flag = False
    
#     return flag

# def check_col(check_board : list[list[str]]) -> bool:
#     flag = True
    
#     transpose_lst = [list(x) for x in zip(*check_board)]

#     for row_num in transpose_lst:
#         li = [] 
#         for row_ele in row_num:
#             if row_ele != ".":
#                 li.append(row_ele)
#         lst_num = len(li)
#         set_num = len(set(li))

#         if lst_num != set_num:
#             flag = False
    
#     return flag

# print(check_row(board))
# print(check_col(board))