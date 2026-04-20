class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        def backtrack(path,used):
            if len(nums) == len(path[:]):
                result.append(path[:])
                return result
            for i in range(0,len(nums)):
                if used[i]==True:
                    continue
                used[i] = True
                path.append(nums[i]) # take 
                backtrack(path,used) #explore
                path.pop() #backtrack
                used[i]=False
        backtrack([],used)
        return result
            
            