"""
A string S containing only the letters "A", "B" and "C" is given. The string can be transformed by removing one occurrence of  "AA", "BB" or "CC".

Transformation of the string is the process of removing letters from it, based on the rules described above. As long as at least one rule can be applied, the process should be repeated. If more than one rule can be used, any one of them could be chosen.

Write a function:

class Solution { public String solution(String S); }

that, given a string S consisting of N characters, returns any string that can result from a sequence of transformations as described above.

For example, given string S = "ACCAABBC" the function may return "AC", because one of the possible sequences of transformations is as follows:

Also, given string S = "ABCBBCBA" the function may return "", because one possible sequence of transformations is:

Finally, for string S = "BABABA" the function must return "BABABA", because no rules can be applied to string S.

Write an efficient algorithm for the following assumptions:

the length of string S is within the range [0..50,000];
string S is made only of the following characters: 'A', 'B' and/or 'C'.
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    """
    1. 현재 원소에서 오른쪽 한칸 원소가 같은지 체크
    2. 만약 같다면 현재 원소랑 오른쪽 원소 제거 
    3. 중복이 없을 때 까지 반복(index 사용해서)
    """
    S = list(S)

    idx = 0 
    while True:
        if len(S) == idx+1:
            break 
        
        elif len(S) == 0:
            return ""
            break
        
        if idx <= len(S):
            if S[idx] == S[idx+1]:
                S.pop(idx)
                S.pop(idx)
                idx = 0 
            else:
                idx += 1 

    return "".join(S)

S = "ACCAABBC"
S = "BABABA"
S = "ABCBBCBA"
print(solution(S))

# 50% 정답...