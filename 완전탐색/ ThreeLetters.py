"""
Write a function solution that, given two integers A and B, returns a string containing exactly A letters 'a' and exactly B letters 'b' with no three consecutive letters being the same (in other words, neither "aaa" nor "bbb" may occur in the returned string).

Examples:

1. Given A = 5 and B = 3, your function may return "aabaabab". Note that "abaabbaa" would also be a correct answer. Your function may return any correct answer.

2. Given A = 3 and B = 3, your function should return "ababab", "aababb", "abaabb" or any of several other strings.

3. Given A = 1 and B = 4, your function should return "bbabb", which is the only correct answer in this case.

Assume that:

A and B are integers within the range [0..100];
at least one solution exists for the given A and B.
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    """
    1. A와 B의 카운트 중 어떤 것이 더 큰지 판별
    2. 큰 부분 부터 먼저 입력 진행 
    3. 동일 문자 카운트가 2가 되면 다른 문자 append
    4. 뭔가 있는데 생각 안남 
    """
    from collections import deque

    A_str = ["a"]*A
    B_str = ["b"]*B

    A_str = deque(A_str)
    B_str = deque(B_str)
    
    return_str = ""
    while len(A_str) != 0 or len(B_str) != 0:
        if len(return_str) >= 2:
            if return_str[-1] == return_str[-2]:
                if return_str[-1] == "a":
                    return_str += B_str.pop()
                elif return_str[-1] == "b":
                    return_str += A_str.pop()
            else:
                if len(A_str) >= len(B_str):
                    return_str += A_str.pop()
                else:
                    return_str += B_str.pop()
            
        else:
            if len(A_str)>=len(B_str):
                return_str += A_str.pop()
            else:
                return_str += B_str.pop()

    print(A_str, B_str)
    return return_str

print(solution(3,3))

# 정답!