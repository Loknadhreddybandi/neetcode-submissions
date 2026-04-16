class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(mid):
            day = 1
            summ = 0
            for x in weights:
                if summ + x > mid: # it exceeds so we need to start ship from next day
                    day +=1
                    summ = 0
                summ = summ + x
            if day<=days:
                return True
            else:
                return False
        low = max(weights)
        high = sum(weights)
        while low<high:
            mid = (low+high)//2
            if feasible(mid):
                high = mid
            else:
                low = mid+1
        return low