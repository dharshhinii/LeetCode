class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        r=l=0
        z=0
        mm=0
        while r<len(nums):
            if nums[r]==0:
             z+=1
            if z<=k:
                m=r-l+1
                mm=max(m,mm)
            while z>k:
                if nums[l]==0:
                    z-=1
                l+=1
            r+=1
        return mm
