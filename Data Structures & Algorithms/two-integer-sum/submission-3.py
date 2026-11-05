class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}

        for i, n in enumerate(nums):
            if (target - n) in difference:
                return [difference[(target - n)], i]
            else:
                difference[n] = i
