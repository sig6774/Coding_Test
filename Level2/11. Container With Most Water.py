"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

"""
1. length의 2개 원소 중 첫번째 원소, 두번쨰 원소 추출
2. 그 이후 그 사이 간격 길이 추출 
3. 1,2 번째 원소 중 작은 값 추출 
4. 2,3번에서 추출한 값을 곱하여 input으로 받은 height 사이에 최대 값 추출 
"""

from typing import List


height = [1,8,6,2,5,4,8,3,7]
height = [1,2]
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_container = -99999
        for idx_1 in range(len(height)):
            tmp_container = -99999
            for idx_2 in range(idx_1+1, len(height)):
                tmp_width = idx_2-idx_1
                tmp_height = min(height[idx_1], height[idx_2])
                tmp_value = tmp_width * tmp_height
                if tmp_container < tmp_value:
                    tmp_container = tmp_value
            
            if max_container < tmp_container:
                max_container = tmp_container
        
        return max_container
    
# print(Solution().maxArea(height))
# timeout 

# 반으로 쪼개서 다시 생각 
# 왜냐면 width값이 커야 최대 값이 나옴
"""
1. length의 2개 원소 중 첫번째 원소, 두번쨰 원소 추출
2. 그 이후 그 사이 간격 길이 추출 
3. 1,2 번째 원소 중 작은 값 추출 
3.1 1번째 원소 추출하는 것은 height의 len //2 까지 작업하도록 진행
4. 2,3번에서 추출한 값을 곱하여 input으로 받은 height 사이에 최대 값 추출 
"""

# height = [1,2]
# height = [1,2,3,1000,9]
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_container = -99999
        for idx_1 in range(len(height)//2):
            tmp_container = -99999
            print(idx_1)
            for idx_2 in range(idx_1+1, len(height)):
                tmp_width = idx_2-idx_1
                tmp_height = min(height[idx_1], height[idx_2])
                tmp_value = tmp_width * tmp_height
                if tmp_container < tmp_value:
                    tmp_container = tmp_value
            
            if max_container < tmp_container:
                max_container = tmp_container
        
        return max_container
    
# print(Solution().maxArea(height))
# 이렇게 하면 다른 예외 케이스에서 걸림 
# 반 이상일 때 최대 값이 나오는 경우 존재 

# log(n)이 나오면서 체크하려면 어떻게 해야하지...?
"""
1. 첫번째 원소는 오른쪽으로 가는데 기준이 그 앞의 원소보다 작을 때 
2. 두번쨰 원소는 왼쪽으로 가는데 기준이 그 전의 원소보다 작을 때
3. loop
"""
height= [8,7,2,1]
height = [1,8,6,2,5,4,8,3,7]
# height = [1,2]
height =[3,6,1]
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_container = -99999
        left_idx, right_idx = 0, len(height)-1

        if len(height) == 2:
            tmp_width = right_idx-left_idx
            tmp_height = min(height[left_idx], height[right_idx])
            tmp_value = tmp_width * tmp_height
            return tmp_value
        else:

            for _ in range(len(height)):
                print(left_idx, right_idx)
                tmp_width = right_idx-left_idx
                tmp_height = min(height[left_idx], height[right_idx])
                tmp_value = tmp_width * tmp_height

                if tmp_value > max_container:
                    max_container = tmp_value

                if height[left_idx] < height[left_idx+1]:
                    left_idx += 1
                elif height[right_idx] < height[right_idx-1]:
                    right_idx -= 1
                
            return max_container
print(Solution().maxArea(height))
# 이렇게 해도 안됨... 
# 기준을 어떻게 줘야하지....

# 직사각형을 만들 때 너비와 높이가 둘 다 커야함

# 참고 풀이 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left=0
        right=len(height)-1
        max_area=0
        while (right-left>0) :
            max_area=max(max_area,(right-left)*min(height[left],height[right]))
                
            if height[left]>=height[right]: # The right is shorter than left
                right-=1
            else: # The left is shorter than right
                left+=1
            
        return max_area

# 포인터를 옮겨서 하는 것은 맞지만 비교 기준 설정에서 차이가 있네...
# while문으로 전체 순회를 하지 않아도 되는 부분도 포함