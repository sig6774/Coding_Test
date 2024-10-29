"""
Is Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
"""

s = "racecar" 
t = "carracq"

s_1 = sorted(s)
# print(s_1)
t_1 = sorted(t)
# print(t_1)

check = True
for idx in range(len(s_1)):
    if s_1[idx] != t_1[idx]:
        check = False        

print(check)

"""
정렬한 후 각 값을 개별 비교 
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = True

        # 각 문자의 개수가 다른 경우도 존재함 
        if len(s) == len(t):
            s_1 = sorted(s)
            t_1 = sorted(t)

            for idx in range(len(s_1)):
                if s_1[idx] != t_1[idx]:
                    check = False
                
            return check


        else:
            check = False 
            return check 