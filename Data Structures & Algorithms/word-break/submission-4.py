class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}
        
        def dfs(start_index: int) -> bool:
            if start_index in memo:
                return memo[start_index]
            if start_index == len(s):
                return True

            for end_index in range(start_index, len(s)):
                if s[start_index: end_index + 1] in wordSet and dfs(end_index + 1):
                    memo[start_index] = True
                    return True
            
            memo[start_index] = False
            return False

        return dfs(0)
