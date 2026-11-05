class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.max_length = 0

        def dfs(start: int, curr_length: int) -> None:
            self.max_length = max(self.max_length, curr_length)

            for i in range(start + 1, len(nums)):
                if nums[start] < nums[i]:
                    dfs(i, curr_length + 1)

        for i in range(len(nums)):
            dfs(i, 1)

        return self.max_length
