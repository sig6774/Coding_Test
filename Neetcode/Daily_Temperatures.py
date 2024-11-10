"""
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
Constraints:
1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100
"""

"""
1. 각 i번째 요소를 popleft를 통해 추출 
2. 추출한 요소와 추출된 리스트의 원소와 비교해서 리스트 원소가 커지는 순서 정보 추출 
3. 추출한 정보 리스트에 append
"""

# from collections import deque
# temperatures = [30,38,30,36,35,40,28]
# deque_temp = deque(temperatures)

# result_lst = []
# while deque_temp:
#     ext_ele = deque_temp.popleft()
#     cnt = 1

#     if len(deque_temp) != 0 and max(deque_temp) > ext_ele:
#         for ele in deque_temp:
#             if ext_ele > ele:
#                 cnt += 1
#             else:
#                 break
#     else:
#         cnt = 0
#     result_lst.append(cnt)

# print(result_lst)

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        from collections import deque

        deque_temp = deque(temperatures)

        result_lst = []

        while deque_temp:
            ext_ele = deque_temp.popleft()
            cnt = 1

            if len(deque_temp) != 0 and max(deque_temp) > ext_ele:
                for ele in deque_temp:
                    if ext_ele >= ele:
                        cnt += 1
                    else:
                        break
            else:
                cnt = 0
            result_lst.append(cnt)

        return result_lst

a = Solution()
temperatures = [30,38,30,36,35,40,28]
temperatures = [22,21,20]
temperatures=[89,62,70,58,47,47,46,76,100,70]
print(a.dailyTemperatures(temperatures = temperatures))
