"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
"""

"""
1. 3중 반복문을 사용해서 그 index 값이 합쳤을 때 0일 경우 그 element를 리스트에 append
"""

# nums = [-1,0,1,2,-1,-4]
# total_lst = []
# flag = True

# for first_idx in range(len(nums)):
#     for second_idx in range(first_idx, len(nums)):
#         for third_idx in range(second_idx, len(nums)):
#             if nums[first_idx] + nums[second_idx] + nums[third_idx] == 0 and first_idx != second_idx and second_idx != third_idx and third_idx != first_idx:
#             # if nums[first_idx] + nums[second_idx] + nums[third_idx] == 0:
#                 lst = [nums[first_idx], nums[second_idx], nums[third_idx]]
#                 sort_lst = sorted(lst)
#                 for idx in range(len(total_lst)):
#                     if total_lst[idx] == sort_lst:
#                         flag = False
#                 if flag:
#                     total_lst.append(sort_lst)
# print(total_lst)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        total_lst = []
        flag = True

        for first_idx in range(len(nums)):
            for second_idx in range(first_idx, len(nums)):
                for third_idx in range(second_idx, len(nums)):
                    if nums[first_idx] + nums[second_idx] + nums[third_idx] == 0 and first_idx != second_idx and second_idx != third_idx and third_idx != first_idx:
                    # if nums[first_idx] + nums[second_idx] + nums[third_idx] == 0:
                        lst = [nums[first_idx], nums[second_idx], nums[third_idx]]
                        sort_lst = sorted(lst)
                        # print(sort_lst)

                        if sort_lst not in total_lst:
                            total_lst.append(sort_lst)
        
        return total_lst
        
nums = [-1,0,1,2,-1,-4]
nums = [0,1,1]
nums=[-1,0,1,2,-1,-4,-2,-3,3,0,4]

a = Solution()
print(a.threeSum(nums))
