class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path,index):
            result.append(path[:])
            for i in range(index,len(nums)):
                curr = nums[i]
                path.append(curr)
                backtrack(path,i+1)
                path.pop()
        backtrack([],0)
        return result

        