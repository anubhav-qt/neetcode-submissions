class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n0, n1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            n0, n1 = n1, max(n1, nums[i] + n0)

        return n1
