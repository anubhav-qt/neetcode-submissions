class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        # prefix product excluding current element
        pp = [1] * length
        for i in range(1, length):
            pp[i] = pp[i - 1] * nums[i - 1]
        
        # suffix product excluding current element
        sp = [1] * length
        for i in range(length - 2, -1, -1):
            sp[i] = sp[i + 1] * nums[i + 1]
        
        return [pp[i] * sp[i] for i in range(length)]
