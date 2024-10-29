"""
Two Integer Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
"""

"""
중첩 반복문으로 인덱스 2개를 통해 합쳤을 때 target과 같다면 종료하도록 구성 
OOM 문제 발생
"""
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         new_list = []

#         for first_idx in range(len(nums)):
#             for second_idx in range(first_idx+1, len(nums)):
#                 print(first_idx, second_idx)
#                 if nums[first_idx] + nums[second_idx] == target:
#                     new_list.append(first_idx)            
#                     new_list.append(second_idx)
#                     break
        
#         return new_list

"""
target에서 첫번쨰 인덱스의 값을 뺀 값이 리스트에 존재하는지 파악 후 있으면 인덱스 추출 후 종료
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        new_list = []

        for idx in range(len(nums)):
            minus_value = target - nums[idx]

            for idx_2 in range(idx+1, len(nums)):
                if minus_value == nums[idx_2]:
                    new_list.append(idx)
                    new_list.append(idx_2)
                    break
        
        return new_list

nums=[4,5,6]
target=10

q = Solution()
print(q.twoSum(nums, target))

