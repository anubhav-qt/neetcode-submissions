class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        possible_values = set([0])

        for num in nums:
            if target in possible_values:
                return True

            temp = possible_values.copy()
            for value in temp:
                if value + num <= target:
                    possible_values.add(value + num)
            possible_values.add(num)
        
        return (target in possible_values)
