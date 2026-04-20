class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        used = [False]*len(nums)
        def backtrack(path,used):
            if len(nums)==len(path[:]):
                result.append(path[:])
                return 
            for i in range(0,len(nums)):
                if used[i]== True: #already in path this value skip
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]: #duplicates at same level skip
                    continue
                used[i]=True
                path.append(nums[i]) #take
                backtrack(path,used) #explore
                path.pop() #backtrack
                used[i]=False
        backtrack([],used)
        return result
                