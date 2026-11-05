# Memoization
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}
        def backtrack(stair: int) -> int:
            if stair >= len(cost):
                return 0
            if stair in self.memo:
                return self.memo[stair]
            
            self.memo[stair] = cost[stair] + min(backtrack(stair + 1), backtrack(stair + 2))
            return self.memo[stair]

        return min(backtrack(0), backtrack(1))
