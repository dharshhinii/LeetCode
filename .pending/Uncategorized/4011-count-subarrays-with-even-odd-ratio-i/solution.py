class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        c=0
        n=len(nums)
        for i in range(n):
          x=y=0
          for j in range(i,n):
            if nums[j]%2==0:
                x+=1
            else:
                y+=1
            if y>0 and x/y<=a/b:
                c+=1
        return c