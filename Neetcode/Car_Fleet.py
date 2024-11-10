# """
# There are n cars traveling to the same destination on a one-lane highway.

# You are given two arrays of integers position and speed, both of length n.

# position[i] is the position of the ith car (in miles)
# speed[i] is the speed of the ith car (in miles per hour)
# The destination is at position target miles.

# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

# Return the number of different car fleets that will arrive at the destination.

# Example 1:

# Input: target = 10, position = [1,4], speed = [3,2]

# Output: 1
# Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

# Example 2:

# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

# Output: 3
# Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

# Constraints:

# n == position.length == speed.length.
# 1 <= n <= 1000
# 0 < target <= 1000
# 0 < speed[i] <= 100
# 0 <= position[i] < target
# All the values of position are unique.
# """

# """
# 1. target_value와 position[i] value를 뺀 값을 새로운 리스트에 저장 
# 2. 새로운 리스트[i]와 speed[i]를 나눠서 몫을 리스트에 저장 
# 3. 중복 제거 후 남은 리스트 개수 출력
# """

# # target = 10
# # position = [4,1,0,7]
# # speed = [2,2,1,1]

# # target = 10
# # position = [1,4]
# # speed = [3,2]

# # minus_lst = [target-ele for ele in position]

# # divide_lst = []

# # for minus_ele, speed_ele in zip(minus_lst, speed):
# #     divide_lst.append(minus_ele // speed_ele)
# # print(divide_lst)
# # print(len(set(divide_lst)))


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        minus_lst = [target-ele for ele in position]

        divide_lst = []

        for minus_ele, speed_ele in zip(minus_lst, speed):
            divide_lst.append(minus_ele // speed_ele)

        print(minus_lst)
        print(divide_lst)        
        return len(set(divide_lst))

target = 10
position = [4,1,0,7]
speed = [2,2,1,1]

target = 10
position = [1,4]
speed = [3,2]

target=12
position=[10,8,0,5,3]
speed=[2,4,1,1,3]

a = Solution()

print(a.carFleet(target = target, position = position, speed = speed))
# 틀림 

# 참고 자료
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - pos) / spd for pos, spd in cars]
        
        fleets = 0
        last_time = 0
        
        for time in times:
            if time > last_time:  
                fleets += 1
                last_time = time  
                
        return fleets

# 테스트 케이스
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

a = Solution()
print(a.carFleet(target, position, speed))  # 출력: 3
