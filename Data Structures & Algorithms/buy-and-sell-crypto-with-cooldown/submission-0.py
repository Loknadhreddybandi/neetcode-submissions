class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(index,have):
            if index >= len(prices):
                return 0
            if (index,have) in memo:
                return memo[(index,have)]
            if have:
                sell = dfs(index+2,False) + prices[index]
                skip = dfs(index+1,True)
                memo[(index,have)] =  max(skip,sell)
            else:
                buy = dfs(index+1,True) - prices[index]
                skip = dfs(index+1,False)
                memo[(index,have)] =  max(buy,skip)
            return memo[(index,have)]
        return dfs(0,False)
        