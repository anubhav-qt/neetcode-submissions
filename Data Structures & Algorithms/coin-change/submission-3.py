class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(remaining_amount: int) -> (int, int):
            """Returns minimum number of coins needed for reaching 'remaining_amount'"""
            if remaining_amount in memo:
                return memo[remaining_amount]
            if remaining_amount < 0:
                return -1
            if remaining_amount == 0:
                return 0

            min_coins = float("inf")
            for coin in coins:
                curr_coins = dfs(remaining_amount - coin)
                if curr_coins != -1:
                    min_coins = min(min_coins, curr_coins + 1)

            memo[remaining_amount] = min_coins if min_coins != float("inf") else -1
            return memo[remaining_amount]

        return dfs(amount)
