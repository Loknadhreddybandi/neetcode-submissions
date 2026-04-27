class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}
        def dfs(index):
            if index == len(s):
                return True
            if (index) in memo:
                return memo[index]
            for end in range(index+1,len(s)+1):
                word = s[index:end]
                if word in wordDict:
                    if dfs(end):
                        memo[index] = True
                        return True
            memo[index] = False
            return False
        return dfs(0)
        