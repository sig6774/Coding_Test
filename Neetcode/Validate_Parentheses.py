"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true

Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
"""

"""
1. 각 괄호의 닫는 기호와 여는 기호 맵핑 
2. 특정 기호와 매칭되는 것이 존재한다면 pop 
3. 마지막에 pop했을 때 값이 있으면 false 
"""

# s = "([{}])"

# map_st = {"}" : "{", ")" : "(", "]" : "["}

# pop_lst = []
# for ele in s:
#     if ele in map_st:
#         if pop_lst[-1] == map_st[ele]:
#             pop_lst.pop()
#     else:
#         pop_lst.append(ele)

# if len(pop_lst) == 0:
#     print("True")
# else:
#     print("False")

class Solution:

    def __init__(self):
        self.map_str = {"}" : "{", ")" : "(", "]" : "["}

    def isValid(self, s: str) -> bool:
        pop_lst = []
        if len(s) > 1:   

            for ele in s:
                if ele in self.map_str:
                    if len(pop_lst) > 0 and pop_lst[-1] == self.map_str[ele]:
                        pop_lst.pop()
                    else:
                        pop_lst.append(ele)
                else:
                    pop_lst.append(ele)

        else:
            pop_lst.append(s)

        if len(pop_lst) == 0:
            return True
        else:
            return False

s = "([{}])"
s = "[(])"
s= "]]"
a = Solution()
print(a.isValid(s))