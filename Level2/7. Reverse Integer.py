"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""

x = -123 
x = 120


class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            str_x = str(abs(x))
            str_x = str_x[::-1]
            str_x = f'-{str_x}'
        else:
            str_x = str(x)
            str_x = str_x[::-1]
        
        check_value = int(str_x)
        
        if check_value <= -2**31 or check_value >= 2**31-1:
            return 0
        else:
            return check_value
