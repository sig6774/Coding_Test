"""
An integer K and a non-empty array A consisting of N integers are given.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A.

A bounded slice is a slice in which the difference between the maximum and minimum values in the slice is less than or equal to K. More precisely it is a slice, such that max(A[P], A[P + 1], ..., A[Q]) − min(A[P], A[P + 1], ..., A[Q]) ≤ K.

The goal is to calculate the number of bounded slices.

For example, consider K = 2 and array A such that:

    A[0] = 3
    A[1] = 5
    A[2] = 7
    A[3] = 6
    A[4] = 3

content_copy
There are exactly nine bounded slices: (0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3), (4, 4).

Write a function:

def solution(K, A)
content_copy

that, given an integer K and a non-empty array A of N integers, returns the number of bounded slices of array A.

If the number of bounded slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given:

    A[0] = 3
    A[1] = 5
    A[2] = 7
    A[3] = 6
    A[4] = 3

content_copy
the function should return 9, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
K is an integer within the range [0..1,000,000,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

"""

"""
1. 완전 탐색으로 풀면 될 것 같은데 
"""
def solution(K, A):
    search_num = len(A)
    cnt = 0
    for first_idx in range(search_num):
        min_v = A[first_idx]
        max_v = A[first_idx]
        for second_idx in range(first_idx, search_num):
            min_v = min(min_v, A[second_idx])
            max_v = max(max_v, A[second_idx])
            if max_v - min_v <= K:
                cnt += 1
    
    if cnt >= 1000000000:
        cnt = 1000000000
    
    return cnt
K = 2
A = [3, 5, 7, 6, 3]
print(solution(K,A))