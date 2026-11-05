class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def backtrack(start_index: int) -> int:
            if start_index in memo:
                return memo[start_index]
            if start_index == len(s):
                return 1

            res = 0
            if s[start_index] != '0':
                res += backtrack(start_index + 1)
                if start_index + 1 < len(s) and '10' <= s[start_index: start_index + 2] <= '26':
                    res += backtrack(start_index + 2)

            memo[start_index] = res
            return res

        return backtrack(0)
