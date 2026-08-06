class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        sm=[1]*n
       
        s=p=1
        for i in range(n-1,-1,-1):
            sm[i]=s        
            s*=nums[i]
        for i in range(n):
            sm[i]=p*sm[i]
            p*=nums[i]
        return sm