"""
You are given an integer array heightss where heightss[i] represents the heights of the 
i th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:

Input: heights = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: heights = [2,2,2]

Output: 4
Constraints:

2 <= heights.length <= 1000
0 <= heights[i] <= 1000
"""

"""
1. i번째와 j 번째 중 값이 같거나 작은 element 찾기
2. j번째에서 i번째를 뺀 값 찾기
3. 1~2번에서 찾은 값 곱하여 임시 변수에 넣고 max 값과 비교 
"""

# max_val = 0
# heights = [1,7,2,5,4,7,3,6]
# heights = [2,2,2]

# for first_idx in range(len(heights)):
#     for second_idx in range(first_idx, len(heights)):
#         min_height = min(heights[first_idx], heights[second_idx])
#         diff_val = second_idx - first_idx

#         temp_val = min_height * diff_val

#         if max_val <= temp_val:
#             max_val = temp_val

# print(max_val)
        

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        
        max_val = 0

        for first_idx in range(len(heights)):
            for second_idx in range(first_idx, len(heights)):
                min_height = min(heights[first_idx], heights[second_idx])
                diff_val = second_idx - first_idx

                temp_val = min_height * diff_val

                if max_val <= temp_val:
                    max_val = temp_val
        
        return max_val

heights = [1,7,2,5,4,7,3,6]
# heights = [2,2,2]
a = Solution()
print(a.maxArea(heights))