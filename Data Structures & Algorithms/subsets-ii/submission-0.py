class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()                       
        
        def backtrack(path, state):
            result.append(path[:])
            
            for i in range(state, len(nums)):
                if i > state and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
            