class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[0]*n for j in range(m)]
        fl=False
        for i in range(n):
            if  fl==True:
                dp[0][i]=1
            if text2[0]==text1[i]:
                dp[0][i]=1
                fl=True
        for i in range(1,m):
            for j in range(n):
                if text2[i]==text1[j]: 
                  if j>0:
                    dp[i][j]=dp[i-1][j-1]+1
                  else:
                    dp[i][j]=1
                else:
                    if j>0:
                       dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                    else:
                        dp[i][j]=dp[i-1][j]
        return dp[-1][-1]