class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(index: int, prev_index: int) -> int:
            if index == len(nums):
                return 0
            if (index, prev_index) in memo:
                return memo[(index, prev_index)]

            skip = dfs(index + 1, prev_index)
            take = 1 + dfs(index + 1, index) if ((prev_index == -1 ) or (nums[index] > nums[prev_index])) else 0

            memo[(index, prev_index)] = max(skip, take)
            return memo[(index, prev_index)]

        return dfs(0, -1)
