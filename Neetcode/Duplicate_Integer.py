"""
Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""

"""
set을 통해 기존 리스트의 개수와 set 개수가 다르면 true 
"""
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        
        init_cnt = len(nums)

        remove_dup_cnt = len(set(nums))

        if init_cnt == remove_dup_cnt:
            return False
        else:
            return True