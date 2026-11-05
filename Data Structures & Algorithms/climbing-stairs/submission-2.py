# Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        def backtrack(stair: int) -> int:
            if stair > n:
                return 0
            if stair == n:
                return 1
            
            if stair in self.memo:
                return self.memo[stair]

            self.memo[stair] = backtrack(stair + 1) + backtrack(stair + 2)
            return self.memo[stair]
        
        return backtrack(0)
