class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=[]
        l=[]
      
        def f(i):
           
            if i==n:
                ans.append(l[:])
                return 
            l.append(nums[i])
            f(i+1)
            while i>0 and  nums[i-1]==nums[i]:
                i+=1
    
            l.pop()
            f(i+1)
            return
        f(0)
        return ans