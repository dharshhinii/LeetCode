class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        l=0
        m=float('inf')
        for j in range(len(nums)):
            s+=nums[j]
            while s>=target:
                m=min(j-l+1,m)
                s-=nums[l]
                l+=1
        return 0 if m==float('inf') else m