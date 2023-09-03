'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

EXAMPLE 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

EXAMPLE 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''
'''
TIME COMPLEXITY: O(N)
- Traverses array N times

SPACE COMPLEXITY: O(1)
- Declares a few variables that require constant space
'''
class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        start = 0
        scout = 1

        while scout < len(prices):
            if prices[start] < prices[scout]:
                profit = prices[scout] - prices[start]
                max_profit = max(max_profit, profit)
            else:
                start = scout
            scout += 1
        return max_profit