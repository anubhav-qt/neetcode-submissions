class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start_index: int, curr_elements: List[int], total: int) -> None:
            if target == total:
                res.append(curr_elements.copy())
                return
            if total > target or start_index >= len(candidates):
                return

            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                curr_elements.append(candidates[i])
                backtrack(i + 1, curr_elements, total + candidates[i])
                curr_elements.pop()

        backtrack(0, [], 0)
        return res
