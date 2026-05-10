"""
A positive integer N is given. The goal is to find the highest power of 2 that divides N. In other words, we have to find the maximum K for which N modulo 2^K is 0.

For example, given integer N = 24 the answer is 3, because 2^3 = 8 is the highest power of 2 that divides N.

Write a function:

class Solution { public int solution(int N); }
content_copy

that, given a positive integer N, returns the highest power of 2 that divides N.

For example, given integer N = 24, the function should return 3, as explained above.

Assume that:

N is an integer within the range [1..1,000,000,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""

"""
1. 2로 몇번 나눠지는지 개수 count 
"""

N = 1000000000 
def solution(N):
    cnt = 0
    while N % 2 == 0:
        cnt += 1 
        N = N // 2 

    return cnt 

print(solution(N))
