"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""

"""
1. 중복 element 제거 및 오름차순 정렬
2. max length(최종 길이 저장), length(임시 길이 저장) 변수 선언
3. 반복문을 통해 현재 element 값과 하나 이전의 element 값을 빼서 1이 나오면 length + 1
4. 1이 나오지 않으면 다시 length 1로 변경
"""

# nums = [2,20,4,10,3,4,5]
# nums = [0,3,2,5,4,6,1,1]
# set_nums = set(nums)
# nums = list(set_nums)

# max_length = 0 
# length = 1 

# for idx in range(len(nums)):
#     if idx > 0:
#         pre_val = nums[idx-1]
#         val = nums[idx]

#         if val - pre_val == 1:
#             # print(pre_val, val)
#             length += 1

#     if max_length < length:
#         max_length = length
#     else:
#         length = 1 
# print(max_length)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        if len(nums) > 0:
            max_length = 0 
            length = 1 

            set_nums = set(nums)
            sort_nums = sorted(set_nums)
            nums = list(sort_nums)
            # print(nums)

            for idx in range(len(nums)):
                if idx > 0:
                    pre_val = nums[idx-1]
                    val = nums[idx]

                    if val - pre_val == 1:
                        length += 1

                    elif max_length <= length:
                        max_length = length
                        length = 1 

                # print(length)

            if max_length < length:
                max_length = length
        
        else:
            max_length = 0

        return max_length

nums=[9,1,4,7,3,-1,0,5,8,-1,6]
# nums = [-1, 0]
# nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
a = Solution()
print(a.longestConsecutive(nums))