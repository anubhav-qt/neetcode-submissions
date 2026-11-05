# space optimized iteration
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        next_max, next_min, global_max = 1, 1, float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            n1, n2, n3 = nums[i], nums[i] * next_max, nums[i] * next_min
            curr_max, curr_min = (max(n1, n2, n3), min(n1, n2, n3))
            global_max = max(global_max, curr_max)
            next_max, next_min = curr_max, curr_min

        return global_max
