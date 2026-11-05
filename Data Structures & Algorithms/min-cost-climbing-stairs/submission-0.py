class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def backtrack(stair: int, curr_cost: int) -> int:
            if stair >= len(cost):
                return curr_cost
            
            return min(backtrack(stair + 1, curr_cost + cost[stair]), backtrack(stair + 2, curr_cost + cost[stair]))
        
        return min(backtrack(0, 0), backtrack(1, 0))

