"""
A positive integer N is given. The goal is to find the highest power of 2 that divides N. In other words, we have to find the maximum K for which N modulo 2^K is 0.

For example, given integer N = 24 the answer is 3, because 2^3 = 8 is the highest power of 2 that divides N.

Write a function:

def solution(N)

that, given a positive integer N, returns the highest power of 2 that divides N.

For example, given integer N = 24, the function should return 3, as explained above.

Assume that:

N is an integer within the range [1..1,000,000,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    """
    1. N의 약수 집합 중 2로 나눠지는 원소 추출 
    2. 추출된 원소 2의 거듭 제곱 애들 찾기
    3. 선택한 원소의 2의 거듭제곱수 값 추출
    """
    max_v, cnt = 0, 0

    for k in range(1, N//2+1):
        if N % k == 0:
            if k % 2 == 0:
                if (k == (k&-k)):
                    # 비트 연산으로 거듭제곱 판별
                    if max_v <= k:
                        max_v = k 
        
    while max_v > 1:
        max_v = max_v // 2
        cnt += 1 
        
    return cnt 

print(solution(2))

# 25% 정답..
