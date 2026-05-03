"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
"""
1. 현재 인덱스의 원소와 그 다음 인덱스간 합을 구해 target과 같다면 인덱스 리턴 
"""

nums = [2,7,11,15]
target = 9

nums = [0,4,3,0]
target = 0

find_lst = None

for idx_1, val_1 in enumerate(nums):
    for idx_2 in range(idx_1+1, len(nums)):
        if val_1 + nums[idx_2] == target:
            find_lst = [idx_1, idx_2]

print(find_lst)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        filter_lst = []

        for idx_1, val_1 in enumerate(nums):
            for idx_2 in range(idx_1+1, len(nums)):
                if val_1 + nums[idx_2] == target:
                    find_lst = [idx_1, idx_2]

        return find_lst
    
# 정답
        
# 참고 풀이 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i