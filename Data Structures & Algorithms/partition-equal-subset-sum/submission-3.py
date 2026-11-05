class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        possible_values = set([0, nums[-1]])

        for i in range(len(nums) - 2, -1, -1):
            if target in possible_values:
                return True

            temp = possible_values.copy()
            for value in temp:
                possible_values.add(value + nums[i])
            possible_values.add(nums[i])
        
        return (target in possible_values)
