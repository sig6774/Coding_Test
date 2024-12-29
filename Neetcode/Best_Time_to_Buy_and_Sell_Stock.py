"""

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100
"""

"""
1. 내림차순 정렬해서 입력으로 받은 리스트와 같은지 비교 
2. 같다면 0을 리턴 
3. 첫번째 인덱스를 기준으로 두번째 인덱스부터 비교해서 첫번째 인덱스보다 크다면 그 값을 빼서 max 값 저장
4. 끝났을 때 max값 리턴
"""

# prices = [10,1,5,6,7,1]
# prices = [10,8,7,5,2]

# sort_prices = sorted(prices, reverse = True)

# max_rslt = -1
# if prices == sort_prices:
#     print(0) 

# else:
#     for idx in range(len(prices)):
#         for two in range(idx, len(prices)):
#             tmp_rslt = 0
#             if prices[idx] < prices[two]:
#                 tmp_rslt = prices[two] - prices[idx]
            
#             if max_rslt < tmp_rslt:
#                 max_rslt = tmp_rslt
                
# print(max_rslt)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        sort_prices = sorted(prices, reverse = True)

        max_rslt = -1
        if prices == sort_prices:
            return 0

        else:
            for idx in range(len(prices)):
                for two in range(idx, len(prices)):
                    tmp_rslt = 0
                    if prices[idx] < prices[two]:
                        tmp_rslt = prices[two] - prices[idx]
                    
                    if max_rslt < tmp_rslt:
                        max_rslt = tmp_rslt
        
            return max_rslt
        