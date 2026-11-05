class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {} # house: backtrack(house)
        def backtrack(house: int) -> int:
            if house >= len(nums):
                return 0
            if house in memo:
                return memo[house]
            
            memo[house] = max(backtrack(house + 1), nums[house] + backtrack(house + 2))
            return memo[house]

        return backtrack(0)
