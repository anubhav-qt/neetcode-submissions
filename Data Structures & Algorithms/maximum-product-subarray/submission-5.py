class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n1_max, n1_min = 1, 1
        global_max = float("-inf")

        for i in range(len(nums) - 1, -1, -1):
            n_max, n_min = float("-inf"), float("inf")
            n_max, n_min = (max(n_max, nums[i], nums[i] * n1_max, nums[i] * n1_min), min(n_min, nums[i], nums[i] * n1_max, nums[i] * n1_min))
            global_max = max(global_max, n_max, n_min)
            n1_max, n1_min = n_max, n_min

        return global_max
