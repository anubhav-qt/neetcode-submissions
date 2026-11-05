# Tabulation 2 pointer
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n0, n1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            n0, n1 = n1, cost[i] + min(n0, n1)
        
        return min(n0, n1)
