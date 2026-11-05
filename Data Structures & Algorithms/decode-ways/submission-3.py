class Solution:
    def numDecodings(self, s: str) -> int:
        mapping_set = set()
        for i in range(1, 27):
            mapping_set.add(str(i))

        memo = {}
        def backtrack(start_index: int) -> int:
            if start_index == len(s):
                return 1
            if start_index > len(s):
                return 0
            if start_index in memo:
                return memo[start_index]

            res = 0
            for end_index in range(start_index, len(s)):
                if end_index - start_index + 1 <= 2 and s[start_index: end_index + 1] in mapping_set:
                    res += backtrack(end_index + 1)
            
            memo[start_index] = res
            return res

        return backtrack(0)
