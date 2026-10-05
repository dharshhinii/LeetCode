class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[float('inf')]*n for i in range(n)]
        
        for i in range(n):
            for j in range(len(triangle[i])):
                if i==0 and j==0:
                    dp[i][j]=triangle[i][j]
                    continue
                if i>0 and j>0:
                    if dp[i-1][j]!=float('inf') and dp[i-1][j]!=float('inf'):
                        dp[i][j]=min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
                    elif dp[i-1][j]!=float('inf'):
                        dp[i][j]=triangle[i][j]+dp[i-1][j]
                    elif  dp[i-1][j-1]!=float('inf'):
                        dp[i][j]=triangle[i][j]+dp[i-1][j-1]
                elif i>0:
                    dp[i][j]=triangle[i][j]+dp[i-1][j]
                    
        return min(dp[-1])