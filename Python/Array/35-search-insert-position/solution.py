class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while i<=j:
            m=(i+j)//2
    
            if nums[m]==target:
                return m
            elif nums[m]>target:
                j=m-1
            else:
              i=m+1
        return i
            