"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""

"""
1. 입력으로 받은 리스트 요소 reverse로 변환 
2. 변환된 리스트를 하나의 문자로 합친 후 형변환(str -> int)
3. 더하기 연산 수행 
4. 수행 결과를 다시 리스트로 변환 
5. 변환된 리스트를 reverse로 변환 
"""
l1 = [2,4,3] 
l2 = [5,6,4]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
l1.reverse()
l2.reverse()

concat_l1 = int("".join(str(ele) for ele in l1))
cocnat_l2 = int("".join(str(ele) for ele in l2))
sum_l1_l2 = str(concat_l1 + cocnat_l2)
print(sum_l1_l2)

reverse_lst = [int(sum_l1_l2[ele]) for ele in range(len(sum_l1_l2)-1,-1, -1)] 
print(reverse_lst)





class Solution:
    def addTwoNumbers(self, l1, l2):
        l1.reverse()
        l2.reverse()
        concat_l1 = int("".join(str(ele) for ele in l1))
        cocnat_l2 = int("".join(str(ele) for ele in l2))

        sum_l1_l2 = str(concat_l1 + cocnat_l2)
        reverse_lst = [int(sum_l1_l2[ele]) for ele in range(len(sum_l1_l2)-1,-1, -1)] 
        return reverse_lst

# 풀긴 풀었는데 linked list로 풀어야해서 다시 풀어야함...






        