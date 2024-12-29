"""
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2], target = 1

Output: 4
Example 2:

Input: nums = [3,5,6,0,1,2], target = 4

Output: -1
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= target <= 1000
"""

"""
1. 리스트의 중간값이 target보다 큰지 작은지 보고 left로 갈지 right로 갈지 판단
2. 판단 후 right라면 -1, left라면 +1을 진행하면서 target과 비교
"""
# nums = [3,4,5,6,1,2]
# target = 1


# left_idx = 0 
# right_idx = len(nums)-1
# while True:
#     if nums[left_idx] == target:
#         print(left_idx)
#         break
    
#     elif nums[right_idx] == target:
#         print(right_idx)
#         break

#     else:
#         left_idx += 1 
#         right_idx -= 1    
    


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left_idx = 0 
        right_idx = len(nums) -1
        
        if len(nums) >= 2:

            while True:
                    
                if nums[left_idx] == target:
                    return left_idx
                    break
                
                elif nums[right_idx] == target:
                    return right_idx
                    break

                else:
                    left_idx += 1 
                    right_idx -= 1

                if left_idx == len(nums) // 2:
                    if nums[left_idx] == target:
                        return left_idx
                        break 

                    else:
                        return -1 
                        break
        else:
            if nums[0] == target:
                return 0
            else:
                return -1

        
nums=[1,3,5]
target=3
a = Solution()
print(a.search(nums = nums, target = target))