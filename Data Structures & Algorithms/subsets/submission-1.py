class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start_index: int, subsets: List[int]) -> None:
            res.append(subsets.copy())

            for i in range(start_index, len(nums)):
                subsets.append(nums[i])
                backtrack(i + 1, subsets)
                subsets.pop()

        backtrack(0, [])
        return res
