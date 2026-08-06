class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c=0
        s=0
        for i in nums:
            if i>0:
                c+=1
            elif i<0:
                s+=1
        return max(c,s)