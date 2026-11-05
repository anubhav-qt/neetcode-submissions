class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr_elements: List[int]) -> None:
            if len(curr_elements) == len(nums):
                res.append(curr_elements.copy())

            for i in range(len(nums)):
                if nums[i] not in curr_elements:
                    curr_elements.append(nums[i])
                    backtrack(curr_elements)
                    curr_elements.pop()
            
        backtrack([])
        return res
