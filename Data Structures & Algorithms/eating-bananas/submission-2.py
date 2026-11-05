import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_valid(num: int) -> bool:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / num)

            return hours <= h

        l, r = 1, max(piles) # O(n)
        res = r

        while l <= r:
            m = l + (r - l) // 2

            if is_valid(m):
                r = m - 1
                res = m
            else:
                l = m + 1
        
        return res
