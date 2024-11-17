"""
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true

Example 2:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000
"""

"""
1. 중첩리스트에 있는 각 리스트의 맨 끝 값을 가지고 target 값과 큰지 작은지 비교
2. 맨 끝 값이 target 값보다 작은 리스트를 발견했을 때 그 리스트에서 중간 값 비교
3. 중간 값이 target 보다 작은지 큰지 비교 후 잘라서 search

굳이 2~3번 하지 않고 1번에서 만족하는 리스트 찾았으면 거기서 in 사용해서 풀면 될 것 같아서 2~3번 제외 
"""
# matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
# target = 10

# flag = False
# for row in range(len(matrix)):
#     if target < matrix[row][-1]:
#         search_lst = matrix[row]
#         break

# if search_lst:
#     if target in search_lst:
#         flag = True

# print(flag)


# if search_lst:
#     mid_idx = len(search_lst) // 2
#     if target == search_lst[mid_idx]:
#         flag = True 

#     else:
#         if target > search_lst[mid_idx]:
#             for idx in range(0, mid_idx):
#                 if target == search_lst[idx]:


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        flag = False
        search_lst = []
        for row in range(len(matrix)):
            if target <= matrix[row][-1]:
                search_lst = matrix[row]
                break
        
        if search_lst:
            if target in search_lst:
                flag = True
            
        return flag

matrix=[[1]]
target=1
a = Solution()
print(a.searchMatrix(matrix = matrix, target = target))