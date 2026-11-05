class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        possible_values = set([0, nums[-1]])

        for i in range(len(nums) - 2, -1, -1):
            temp = possible_values.copy()
            for value in temp:
                possible_values.add(value + nums[i])
            possible_values.add(nums[i])
        
        return ((sum(nums) // 2) in possible_values)
