class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(state,path,remaining):
            if remaining ==0:
                result.append(path[:])
                return 
            if remaining <0: #if i have more remaining means need to explore and get someelement to make remaining 0
                return 
            for i in range(state,len(nums)):
                curr = nums[i]
                path.append(curr)
                backtrack(i,path,remaining-curr)
                path.pop()
        backtrack(0,[],target)
        return result
           