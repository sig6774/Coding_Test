"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
"""

"""
리스트의 고유 원소와 일치하는 개수를 추출
그리고 개수의 내림차순으로 고유 원소 추출
"""
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        def sort_dict_by_value_desc(dict_info : dict) -> dict:
            # value를 기준으로 내림차순 정렬
            return dict(sorted(dict_info.items(), key=lambda item: item[1], reverse=True))

        set_nums = list(set(nums))
        
        check_set = {}
        for num in set_nums:
            local_cnt = 0 
            for n in nums:
                if num == n:
                    local_cnt += 1
            
            check_set[num] = local_cnt
        
        sort_ele = sort_dict_by_value_desc(check_set)

        return list(sort_ele.keys())[:k]

q = Solution()
nums = [1,2,2,3,3,3]
k = 2
print(q.topKFrequent(nums,k))
