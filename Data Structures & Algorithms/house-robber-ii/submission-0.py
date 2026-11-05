# if we start from 0, we go till second last
# else we go till last

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # starting from 0
        n0, n1 = nums[0], nums[0]
        for i in range(2, len(nums) - 1):
            n0, n1 = n1, max(nums[i] + n0, n1)
        
        max_from_zero = max(n0, n1)

        # starting from 1
        n0, n1 = 0, nums[1]
        for i in range(2, len(nums)):
            n0, n1 = n1, max(nums[i] + n0, n1)
        
        max_from_one = max(n0, n1)

        return max(max_from_zero, max_from_one)
