"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

"""
1. 리스트 더하기 연산자로 합침 
2. 더한 리스트의 개수 구한 후 홀수, 짝수 구분 
3. 홀수인 경우 // 2 의 몫을 리턴 
4. 짝수인 경우 // 2 의 몫과 그 몫의 -1 값을 더하여 리턴 
"""

nums1 = [1,2]
nums2 = [3,4]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total_nums = nums1 + nums2 
        total_nums.sort()
        if len(total_nums) > 2:
            if len(total_nums) % 2 == 0:
                median_idx = len(total_nums) // 2
                median_idx_2 = median_idx -1 
                median_value = (total_nums[median_idx] + total_nums[median_idx_2]) / 2
            else: 
                median_idx = len(total_nums) // 2
                median_value = total_nums[median_idx]

        elif len(total_nums) == 2:
            median_value = (total_nums[0] + total_nums[1]) / 2
        else:
            median_value = total_nums[0]

        return median_value




