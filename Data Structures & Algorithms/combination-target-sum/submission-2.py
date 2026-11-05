class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start_index: int, curr_elements: List[int], total: int) -> None:
            if target == total:
                res.append(curr_elements.copy())
                return
            if total > target or start_index >= len(nums):
                return

            for i in range(start_index, len(nums)):
                curr_elements.append(nums[i])
                backtrack(i, curr_elements, total + nums[i])
                curr_elements.pop()
        
        backtrack(0, [], 0)
        return res
