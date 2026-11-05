# if we start from 0, we go till second last
# else we go till last

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper_rob(n0: int, n1: int, nums: List[int]) -> int:
                for i in range(2, len(nums)):
                    n0, n1 = n1, max(nums[i] + n0, n1)
                
                return max(n0, n1)

        return max(helper_rob(nums[0], nums[0], nums[:-1]), helper_rob(0, nums[1], nums))
