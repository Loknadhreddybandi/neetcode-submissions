class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k!=0:
            return False
        target = total//k
        used = [False]*len(nums)
        def backtrack(index,k,subset_sum):
            if k==0:
                return True
            if subset_sum == target: # one bucket filled need to fill k-1 to get k to 0
                return backtrack(0,k-1,0)
            for i in range(index,len(nums)):
                if used[i]==True: #already included
                    continue
                if subset_sum + nums[i]>target: #dont take this look for smaller
                    continue
                #otheriwse curr element is reaching close to target
                used[i]=True
                if backtrack(i+1,k,subset_sum + nums[i]):
                    return True
                used[i]=False
            return False
        return backtrack(0,k,0)
        
            
        