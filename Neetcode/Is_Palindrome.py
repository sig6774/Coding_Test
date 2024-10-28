"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""

"""
1. 모두 소문자 변환 및 띄워쓰기 제거
2. 문자열 개수 구한 후 반으로 자르기
3. 반으로 자른 문자열 첫번째와 두번째 문자열(transpose) 같은지 비교 
4. 같다면 true, 틀리면 false
"""
# s = "abcd cbA"
# s = s.lower()
# s = s.replace(" ", "")
# print(s)
# a = len(s)
# b = a//2
# print(s[:b], s[b+1:])
# q = "".join(reversed(s[b+1:]))
# print(q)

# s = "abccba"
# a = len(s)
# b = a//2
# print(s[:b], s[b:])

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        flag = False

        if len(s) == 1:
            flag = True

        lower_s = s.lower()
        lower_s = lower_s.replace(" ", "")
        check_len = len(lower_s)
        pre_alpha = list(filter(str.isalnum, lower_s))
        only_alpha =''.join(pre_alpha)
        str_len = len(only_alpha)
        print(only_alpha)

        if str_len > 1:
            divide_num = str_len // 2
            front = only_alpha[:divide_num]

            if str_len % 2 == 0:
                back = only_alpha[divide_num:]
            else:
                back = only_alpha[divide_num+1:]
        
            back_transpose = "".join(reversed(back))
            print(front, back_transpose)
            if front == back_transpose:
                flag = True
        
        # elif check_len != str_len and str_len == 1:
        elif str_len == 1:
            flag = True

        else:
            flag = True

        return flag

s = "Was it a car or a cat I saw?"
s=".,"
s="0P"
# s="a."
a = Solution()
print(a.isPalindrome(s))
