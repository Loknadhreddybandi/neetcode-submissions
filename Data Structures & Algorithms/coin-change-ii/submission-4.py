class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def dfs(index,capacity):
            if capacity ==0:
                return 1
            if index >= n:
                return 0
            if (index,capacity) in memo:
                return memo[(index,capacity)]
            skip = dfs(index+1,capacity)
            take = 0
            if coins[index] <= capacity:
                take  =  dfs(index,capacity-coins[index])
            memo[(index,capacity)] = take + skip
            return memo[(index,capacity)]
        return dfs(0,amount)
        