class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        i=-1
        j=-1
        n=len(nums)
        while l<n:
            if nums[l]==target:
               if i==-1:
                 i=l
                 j=l
               else:
                 j=l
            if nums[l]>target:
                break
           
            l+=1
        return [i,j]