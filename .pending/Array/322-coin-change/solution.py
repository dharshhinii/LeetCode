class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[float('inf')]*(amount+1) for i in range(n)]
        dp[0][0]=0
        for i in range(1,amount+1):
           if i%coins[0]==0:
            dp[0][i]=i//coins[0]
        for i in range(1,n):
            for j in range(amount+1):
                if j>0 and j-coins[i]>=0:

                     dp[i][j]=min(dp[i-1][j],dp[i][j-coins[i]]+1)
    
                else:
                    dp[i][j]=dp[i-1][j]
        if dp[-1][-1]==float('inf'):
            dp[-1][-1]=-1
        return dp[-1][-1]