class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(index,path,remaining):
            if remaining ==0:
                result.append(path[:])
                return
            if remaining <0:
                return 
            for i in range(index,len(candidates)):
                #check for dupliacates and skip that index
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path,remaining-candidates[i])
                path.pop()
        backtrack(0,[],target)
        return result
        