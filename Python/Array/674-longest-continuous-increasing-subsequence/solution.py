class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m=c=1
        n=len(nums)
        for  i in range(n-1):
            if nums[i]<nums[i+1]:
                c+=1
            else:
                c=1
            m=max(m,c)
        return m