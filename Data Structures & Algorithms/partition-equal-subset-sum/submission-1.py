class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2
        memo = {}

        def dfs(start: int, curr_sum: int) -> bool:
            if (start, curr_sum) in memo:
                return memo[(start, curr_sum)]
            if curr_sum == half:
                memo[start] = True
                return True
            if start >= len(nums) or curr_sum > half:
                return False

            include = dfs(start + 1, curr_sum + nums[start])
            exclude = dfs(start + 1, curr_sum)

            memo[(start, curr_sum)] = include or exclude
            return memo[(start, curr_sum)]

        return dfs(0, 0)
