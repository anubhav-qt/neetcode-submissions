class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start_index: int, subset: List[int]) -> None:
            res.append(subset.copy())

            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i - 1]:
                    continue
                
                subset.append(nums[i])
                backtrack(i + 1, subset) 
                subset.pop()
        
        backtrack(0, [])
        return res
