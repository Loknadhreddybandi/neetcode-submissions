import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(mid):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours<=h:
                return True
            return False

        low = 1
        high = sum(piles)
        ans = -1
        while low<=high:
            mid = (low+high)//2
            if feasible(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans

        