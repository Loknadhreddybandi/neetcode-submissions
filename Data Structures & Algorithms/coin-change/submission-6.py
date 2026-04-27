class Solution:
    def coinChange(self, coins: List[int], target: int) -> int:
        memo = {}
        n = len(coins)
        def dfs(index, amount):
            if amount == 0:
                return 0
            if index >= n:
                return float('inf')
            if (index,amount) in memo:
                return memo[(index,amount)]

            skip = dfs(index + 1, amount)

            take = float('inf')
            if coins[index] <= amount:
                take = 1 + dfs(index, amount - coins[index])  

            memo[(index,amount)] =  min(skip, take)
            return memo[(index,amount)]

        res = dfs(0, target)
        return res if res != float('inf') else -1