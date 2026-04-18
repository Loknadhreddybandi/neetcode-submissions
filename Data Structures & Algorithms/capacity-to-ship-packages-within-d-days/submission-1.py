class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def feasible(mid):
            day =1
            current_capacity = 0
            for weight in weights:
                if current_capacity + weight > mid:
                    day +=1
                    current_capacity = 0
                current_capacity += weight
            if day<=days:
                return True
            return False

        low = max(weights)
        high = sum(weights)
        ans = -1
        while low<=high:
            mid = (low+high)//2
            if feasible(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
        