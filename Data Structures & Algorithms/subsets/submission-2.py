class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start_index: int, subset: List[int]) -> None:
            res.append(subset.copy())

            for i in range(start_index, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        backtrack(0, [])
        return res
