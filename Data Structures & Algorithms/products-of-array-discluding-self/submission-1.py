class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        res = [1] * length
        for i in range(1, length):
            res[i] = res[i - 1] * nums[i - 1]
        
        # res = 1, 1, 2, 8
        suffix_product = 1
        for i in range(length - 2, -1, -1):
            suffix_product *= nums[i + 1]
            res[i] *= suffix_product
        
        return res
