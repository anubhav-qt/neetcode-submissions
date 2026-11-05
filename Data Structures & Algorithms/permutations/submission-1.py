class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def backtrack(curr_elements: List[int]) -> None:
            if len(curr_elements) == len(nums):
                res.append(curr_elements.copy())

            for i in range(len(nums)):
                if nums[i] not in visited:
                    curr_elements.append(nums[i])
                    visited.add(nums[i])
                    backtrack(curr_elements)
                    curr_elements.pop()
                    visited.remove(nums[i])
            
        backtrack([])
        return res
