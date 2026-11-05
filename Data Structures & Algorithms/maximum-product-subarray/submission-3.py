class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = {}
        self.global_max = float("-inf")

        def dfs(index: int) -> (int, int):
            """Returns the maximum product possible by any subarray starting from that index"""
            if index in memo:
                return memo[index]
            if index >= len(nums):
                return (1, 1)

            max_product, min_product = float("-inf"), float("inf")
            next_max, next_min = dfs(index + 1)
            max_product = max(max_product, nums[index], nums[index] * next_max, nums[index] * next_min)
            min_product = min(min_product, nums[index], nums[index] * next_max, nums[index] * next_min)
            self.global_max = max(self.global_max, max_product, min_product)

            memo[index] = max(max_product, min_product), min(max_product, min_product)
            return (max_product, min_product)

        dfs(0)
        return self.global_max
