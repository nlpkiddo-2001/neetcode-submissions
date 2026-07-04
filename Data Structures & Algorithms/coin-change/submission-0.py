class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for current in range(1, amount + 1):
            for coin in coins:
                if coin <= current:
                    dp_current_minus_coin = dp[current - coin]

                    dp[current] = min(
                        dp[current],
                        1 + dp_current_minus_coin
                    )
        
        return dp[amount] if dp[amount] != INF else -1 
