class Solution:
    def thirdMax(self, nums: List[int]) -> int:
       nums.sort()
       f=min(nums)
       s=t=None
       for i in nums:
         if i>f:
            t=s
            s=f
            f=i
       if t==None:
         return f
       return t