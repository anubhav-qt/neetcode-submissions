from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash_map = defaultdict(int) # for storing the numbers and their indices
        for i, num in enumerate(nums):
            hash_map[num] = i

        res = set()
        for l in range(len(nums)):
            for r in range(l + 1, len(nums)):
                if 0 - (nums[l] + nums[r]) in hash_map and hash_map[0 - (nums[l] + nums[r])] != l and  hash_map[0 - (nums[l] + nums[r])] != r:
                    res.add(tuple(sorted([nums[l], nums[r], 0 - (nums[l] + nums[r])])))
        
        return [triplet for triplet in res]
