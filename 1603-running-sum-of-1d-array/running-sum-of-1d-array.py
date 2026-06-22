class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c=[]
        t=0
        for i in nums:
            t+=i
            c.append(t)
        return c