class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=0
        for i in range(k):
            s+=nums[i]
        m=s
        for i in range(len(nums)-k):
    
            s=s-nums[i]+nums[k+i]
            m=max(s,m)
        return m/k