"""
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1

Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
"""

"""
1. 입력 리스트의 중간 값, index 번호 추출 
2. 만약 중간 값이 target 값보다 크면 중간 아래만 search 
3. 만약 중간 값이 target 값보다 작으면 중간 위 search
"""

# nums = [-1,0,2,4,6,8]
# target = 4 

# save_idx = -1
# mid_idx = len(nums) // 2
# if nums[mid_idx] == target:
#     save_idx = mid_idx
# else:
#     if nums[mid_idx] > target:
#         for idx in range(mid_idx+1, len(nums)):
#             if nums[idx] == target:
#                 save_idx = idx

#     else:
#         for idx in range(0, mid_idx-1):
#             if nums[idx] == target:
#                 save_idx = idx
# print(save_idx)


class Solution:
    def search(self, nums: list[int], target: int) -> int:

        save_idx = -1 

        mid_idx = len(nums) // 2

        if nums[mid_idx] == target:
            save_idx = mid_idx
        
        else:
            if nums[mid_idx] > target:
                for idx in range(0, mid_idx):
                    if nums[idx] == target:
                        save_idx = idx

            else:
                for idx in range(mid_idx, len(nums)):
                    if nums[idx] == target:
                        save_idx = idx

        return save_idx

nums=[-1,0,3,5,9,12]
target=9

a = Solution()
print(a.search(nums, target))