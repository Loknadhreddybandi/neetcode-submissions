class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(mid):
            count = 1
            summ = 0
            for num in nums:
                if summ + num > mid:
                    count +=1
                    summ = 0
                summ += num
            if count <=k:
                return True
            return False
        low = max(nums)
        high = sum(nums)
        ans = -1
        while low<=high:
            mid = (low+high)//2
            if feasible(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans 

        