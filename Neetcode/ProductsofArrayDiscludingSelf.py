"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
"""

"""
1. 왼쪽부터 그 요소를 pop하고 나머지 원소끼리 곱한 결과 append
2. pop한 요소를 다시 맨 오른쪽에 넣고 2번 과정 반복 
3. pop을 입력으로 받은 list 개수만큼 진행했다면 종료 
"""
class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        from collections import deque

        def multiple_lst(nums_dq) -> int:
        
            s = 1
            for n in nums_dq:
                s = s*n
            
            return s 

        
        results = []
        deque_nums = deque(nums)
        for _ in range(len(nums)):
            pop_ele = deque_nums.popleft()
            mul_rslt = multiple_lst(deque_nums)
            results.append(mul_rslt)
            deque_nums.append(pop_ele)
        
        return results


nums = [1,2,4,6]
nums = [-1,0,1,2,3]
a = Solution()
print(a.productExceptSelf(nums))

        
# from collections import deque
# nums = [1,2,4,6]
# q = deque(nums)

# s = 1
# for n in q:
#     s = s*n
# print(s)