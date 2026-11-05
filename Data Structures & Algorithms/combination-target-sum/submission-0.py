class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start_index: int, curr_elements: List[int], total: int) -> None:
            if total == target:
                res.append(curr_elements.copy())
                return

            if start_index >= len(nums) or total > target:
                return

            curr_elements.append(nums[start_index])
            backtrack(start_index, curr_elements, total + nums[start_index])
            curr_elements.pop()
            backtrack(start_index + 1, curr_elements, total)
        
        backtrack(0, [], 0)
        return res
