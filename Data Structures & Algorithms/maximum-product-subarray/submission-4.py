class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [(float("-inf"), float("inf"))] * (len(nums) + 1)
        dp[len(nums)] = (1, 1)
        global_max = float("-inf")
        
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = (max(dp[i][0], nums[i], nums[i] * dp[i + 1][0], nums[i] * dp[i + 1][1]), min(dp[i][1], nums[i], nums[i] * dp[i + 1][0], nums[i] * dp[i + 1][1]))
            global_max = max(global_max, dp[i][0], dp[i][1])

        return global_max
