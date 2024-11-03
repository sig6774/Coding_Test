"""
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5

Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].
"""

"""
1. 사칙 연산 관련 로직 작성 
2. 한 글자마다 append
2. 사칙 연산이 아니라면 리스트에 element append
"""

# tokens = ["1","2","+","3","*","4","-"]

# stack_lst = []
# for ele in tokens:
#     if ele == "+":
#         plus_ele = (int(stack_lst.pop()) + int(stack_lst.pop()))

#         stack_lst.append(plus_ele)

#     elif ele == "-":
#         first_ele = int(stack_lst.pop())
#         second_ele = int(stack_lst.pop())
#         minus_ele = (second_ele - first_ele)

#         stack_lst.append(minus_ele)
    
#     elif ele == "/":
#         first_ele = int(stack_lst.pop())
#         second_ele = int(stack_lst.pop())
#         divide_ele = (second_ele / first_ele)

#         stack_lst.append(divide_ele)

#     elif ele == "*":
#         multiple_ele = (int(stack_lst.pop()) * int(stack_lst.pop()))

#         stack_lst.append(multiple_ele)
    
#     else:
#         stack_lst.append(ele)

# print(stack_lst[0])

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack_lst = []
        for ele in tokens:
            if ele == "+":
                plus_ele = (int(stack_lst.pop()) + int(stack_lst.pop()))

                stack_lst.append(plus_ele)

            elif ele == "-":
                first_ele = int(stack_lst.pop())
                second_ele = int(stack_lst.pop())
                minus_ele = (second_ele - first_ele)

                stack_lst.append(minus_ele)
            
            elif ele == "/":
                first_ele = int(stack_lst.pop())
                second_ele = int(stack_lst.pop())
                divide_ele = (second_ele / first_ele)

                stack_lst.append(divide_ele)

            elif ele == "*":
                multiple_ele = (int(stack_lst.pop()) * int(stack_lst.pop()))

                stack_lst.append(multiple_ele)
            
            else:
                stack_lst.append(ele)

        return int(stack_lst[0])

tokens = ["1","2","+","3","*","4","-"]
a = Solution()

print(a.evalRPN(tokens))