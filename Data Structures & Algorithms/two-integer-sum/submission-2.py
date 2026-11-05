class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}

        for i in range(len(nums)):
            difference[nums[i]] = i
        
        for i in range(len(nums)):
            if (target - nums[i]) in difference and i != difference[(target - nums[i])]:
                return [i, difference[target - nums[i]]]
