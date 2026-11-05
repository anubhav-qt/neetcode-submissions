class Solution:
    def climbStairs(self, n: int) -> int:
        self.res = 0
        def backtrack(stair: int) -> None: # start with 1
            if stair > n:
                return
            if stair == n:
                self.res += 1
                return
            
            backtrack(stair + 1)
            backtrack(stair + 2)
        
        backtrack(0)
        return self.res
