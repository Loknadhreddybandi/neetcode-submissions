class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}
        def dfs(index):
            if index == len(s):
                return True
            if (index) in memo:
                return memo[index]
            
            for end in range(index+1,len(s)+1): #this will be entire string
                word = s[index:end] # end is not include we will get everything upto end-1
                if word in wordDict:
                    #solve for next word
                    if dfs(end):
                        memo[index] = True
                        return memo[index]
            memo[index] = False
            return memo[index]
        return dfs(0)
        