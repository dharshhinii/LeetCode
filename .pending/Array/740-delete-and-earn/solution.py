class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        f=Counter(nums)
        s=sorted(f.keys())
        n=len(s)
        if n==0:
            return 0
        else:
         m=max(s)
         dp=[0]*(m+1)
         dp[0]=0
         
         for i in range(1,m+1):
            if i-2>=0:
                dp[i]=max(dp[i-1],dp[i-2]+(f[i]*i))
           
            else:
                dp[i]=max(dp[i-1],f[i]*i)
  
         return dp[-1]
        