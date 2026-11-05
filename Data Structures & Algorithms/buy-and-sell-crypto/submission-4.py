class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, sell_price = 0, 0
        buy_price = 0
        res = 0

        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            elif prices[r] - prices[l] > res:
                res = prices[r] - prices[l]
            
        return res
