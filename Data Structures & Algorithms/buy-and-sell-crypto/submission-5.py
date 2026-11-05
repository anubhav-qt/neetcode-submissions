class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, profit = 0, 0

        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            elif prices[r] - prices[l] > profit:
                profit = prices[r] - prices[l]
            
        return profit
