class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp  = [[-1] * n for _ in range(n)]

        def dfs(index,have):
            if index >= len(prices):
                return 0
            if dp[index][have] !=-1:
                return dp[index][have]
            if have:
                sell = dfs(index+2,False) + prices[index]
                skip = dfs(index+1,True)
                dp[index][have] =  max(skip,sell)
            else:
                buy = dfs(index+1,True) - prices[index]
                skip = dfs(index+1,False)
                dp[index][have] =  max(buy,skip)
            return dp[index][have]
        return dfs(0,False)
        