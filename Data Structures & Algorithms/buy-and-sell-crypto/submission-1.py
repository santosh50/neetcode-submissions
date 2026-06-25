class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_min = prices[0]
        for i in range(len(prices)):
            curr_min = min(prices[i], curr_min)
            profit = prices[i] - curr_min
            max_profit = max(profit, max_profit)
        return max_profit


            

        