class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n 
        dp[0]=nums[0]
        for i in range(1,n):
           if i-2>=0:
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
           else:
            dp[i]=max(dp[i-1],nums[i])
        return dp[-1]