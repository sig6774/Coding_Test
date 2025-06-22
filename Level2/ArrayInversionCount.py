"""
An array A consisting of N integers is given. An inversion is a pair of indexes (P, Q) such that P < Q and A[Q] < A[P].

Write a function:

class Solution { public int solution(int[] A); }

that computes the number of inversions in A, or returns −1 if it exceeds 1,000,000,000.

For example, in the following array:

 A[0] = -1 A[1] = 6 A[2] = 3
 A[3] =  4 A[4] = 7 A[5] = 4
there are four inversions:

   (1,2)  (1,3)  (1,5)  (4,5)
so the function should return 4.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [-2,147,483,648..2,147,483,647].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    """
    1. 현재 값에서 나보다 작은 값을 찾기(현재 인덱스 이후 기준) 
    2. 찾으면 인덱스 기록
    """
    idx_li = []
    for idx_1 in range(len(A)):
        for idx_2 in range(idx_1+1, len(A)):
            if A[idx_1] > A[idx_2]:
                idx_li.append((idx_1, idx_2))
    
    # print(idx_li)

    if len(idx_li) > 1000000000:
        return -1 
    else:
        return len(idx_li)

A = [-1,5,3,4,7,4]
print(solution(A))

# 63% 정답...