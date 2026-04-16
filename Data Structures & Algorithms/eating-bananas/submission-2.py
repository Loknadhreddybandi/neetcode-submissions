import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(mid):
            total = 0 #this is hours 

            for x in piles:
                total += math.ceil(x/mid)
            if total<=h:
                return True
            return False
        low = 1
        high = max(piles)
        while low<high:
            mid = (low+high)//2
            if feasible(mid):
                high = mid
            else:
                low = mid+1
        return low

        