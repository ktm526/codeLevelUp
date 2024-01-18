#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for x in range(0, len(prices)-1):
            for y in range(x+1, len(prices)):
                if prices[y] - prices[x] > result:
                    result =  prices[y] - prices[x]
        return result