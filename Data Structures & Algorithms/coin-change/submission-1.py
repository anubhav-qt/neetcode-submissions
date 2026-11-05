class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.min_coins = float("inf")

        def dfs(start_index: int, sum_coins: int, coin: int) -> None:
            if coin > self.min_coins:
                return
            if sum_coins == amount:
                self.min_coins = min(self.min_coins, coin)
                return
            if start_index >= len(coins) or sum_coins > amount:
                return

            for i in range(start_index, len(coins)):
                dfs(i, sum_coins + coins[i], coin + 1)

        dfs(0, 0, 0)
        return self.min_coins if self.min_coins != float("inf") else -1
