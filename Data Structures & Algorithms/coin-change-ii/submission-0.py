class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n+1)]
        def dfs(index,target):
            if index==len(coins):
                return 0
            if target == 0 :
                return 1
            if target < 0 :
                return 0
            if dp[index][target]!=-1:
                return dp[index][target]
            take = dfs(index,target-coins[index])  
            nottake = dfs(index+1,target)
            dp[index][target] =  take + nottake
            return dp[index][target]
        return dfs(0,amount)

        