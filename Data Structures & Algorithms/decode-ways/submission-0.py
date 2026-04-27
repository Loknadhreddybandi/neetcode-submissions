class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(index):
            if index == len(s):
                return 1
            if s[index]== "0":
                return 0
            if (index) in memo:
                return memo[index]
            one = dfs(index+1)
            #for two there is a condition
            two = 0
            if (index+1<len(s) and (s[index]=="1" or s[index]=="2" and s[index+1] in "0123456")):
                two =  dfs(index+2)
            memo[index] = one + two
            return memo[index]
        return dfs(0)
        