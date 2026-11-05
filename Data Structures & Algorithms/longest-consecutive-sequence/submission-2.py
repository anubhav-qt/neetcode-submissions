from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        max_length = 0

        for num in all_nums:
            if num - 1 not in all_nums:
                next_num = num + 1
                length = 1

                while next_num in all_nums:
                    length += 1
                    next_num += 1
                
                max_length = max(length, max_length)
        
        return max_length
