"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Constraints:

2 <= numbers.length <= 1000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000
"""

"""
1. 첫번째 원소의 값부터 target에서 뺀 값이 나머지 리스트의 원소 값에 있는지 확인 
2. 그 값이 있다면 해당 원소의 인덱스 추출 
3. 없으면 두번째 원소로 1 번 반복
"""

numbers = [1,2,3,4]
target = 3

def a(numbers):
    for first_idx in range(len(numbers)):
        minus_val = target - numbers[first_idx]
        print(minus_val)
        for second_idx in range(first_idx, len(numbers)):
            if minus_val == numbers[second_idx]:
                return [first_idx+1, second_idx+1]
    
print(a(numbers))

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for first_idx in range(len(numbers)):
            minus_val = target - numbers[first_idx]
            # print(minus_val)
            for second_idx in range(first_idx, len(numbers)):
                if minus_val == numbers[second_idx]:
                    return [first_idx+1, second_idx+1]

a = Solution()

print(a.twoSum(numbers, target))
