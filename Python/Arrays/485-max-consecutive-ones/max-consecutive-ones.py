class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=[]
        s=[]
        s.append(nums[0])
        for i  in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                 s.append(nums[i])
            else:
                l.append(s)
                s=[]
                s.append(nums[i])
        l.append(s)
        m=0
        for i in l:
            if len(i)>m and 1 in i:
                m=len(i)
        return m